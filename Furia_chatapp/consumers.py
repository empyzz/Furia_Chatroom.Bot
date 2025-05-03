from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.core.cache import cache
from channels.db import database_sync_to_async
from .models import PublicMessage, ChatRoom
import traceback
from django.utils import timezone 

import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    # Locale não suportado, segue com o padrão do sistema
    print("pt_BR.UTF-8 não disponível, usando locale padrão.")
    
    
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_slug = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f"chat_{self.room_slug}"
        
        exists = await self.room_exists()
        if not exists:
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        user = self.scope["user"]
        if user.is_authenticated:
            cache.set(f"user_online_{user.id}", True, timeout=60*5)
        await self.accept()

    @database_sync_to_async
    def room_exists(self):
        return ChatRoom.objects.filter(slug=self.room_slug).exists()

    async def disconnect(self, close_code):
        user = self.scope["user"]
        if user.is_authenticated:
            cache.delete(f"user_online_{user.id}")

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            user = self.scope["user"]
            saved_message = await self.save_public_message(message)

            if not saved_message:
                await self.send(text_data=json.dumps({'error': 'Falha ao salvar a mensagem.'}))
                return

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': user.username,
                    'profile_image': user.profile_image.url if user.profile_image else '',
                    'timestamp': timezone.localtime(saved_message.timestamp).strftime("%H:%M"),
                    'data': timezone.localtime(saved_message.timestamp).strftime("%d/%m/%Y"),
                    'user_id': user.id,
                }
            )
        except Exception as e:
            traceback.print_exc()
            await self.close()

        if not saved_message:
            await self.send(text_data=json.dumps({
                'error': 'Erro ao salvar a mensagem. Sala não encontrada.'
            }))
            return
        
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'profile_image': event['profile_image'],
            'timestamp': event['timestamp'],
            'data': event.get('data'),
            'user_id': event['user_id'],
        }))

    @database_sync_to_async
    def save_public_message(self, message):
        try:
            room = ChatRoom.objects.get(slug=self.room_slug)
            saved = PublicMessage.objects.create(
                user=self.scope["user"],
                content=message,
                room=room
            )
            return saved
        except ChatRoom.DoesNotExist:
            print(f"[ERRO] Sala com slug '{self.room_slug}' não encontrada.")
            return None

