from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.http import JsonResponse
from django.core.cache import cache 
from .models import * 
from .utils import get_online_users
from .forms import *
import os, json


def home(request):
    chat_rooms = ChatRoom.objects.all()
    contexto = {
        'chat_rooms': chat_rooms,
        "online_users": get_online_users()
    }
    return render(request, "first.html", contexto)


def profile(request):
    return render(request, 'profile.html')


@csrf_exempt
@login_required
def upload_profile_image(request):
    if request.method == 'POST' and request.FILES.get('profile_image'):
        profile_image = request.FILES['profile_image']
        user = request.user

        user.profile_image = profile_image
        user.save()

        return JsonResponse({
            'profile_image_url': user.profile_image.url,
            'message': 'Imagem atualizada com sucesso'
        })
    return JsonResponse({'error': 'Arquivo não encontrado'}, status=400)

User = get_user_model()
def change_name(request):
    if request.method == 'POST':
        novo_nome = request.POST.get('nome')
        if User.objects.filter(username=novo_nome).exclude(pk=request.user.pk).exists():
            return JsonResponse({'status': 'error', 'message': 'Nome de usuário já está em uso.'}, status=400)

        request.user.username = novo_nome
        request.user.save()
        return JsonResponse({'status': 'ok', 'novo_nome': novo_nome})
    
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'method_not_allowed'}, status=405)


def lista_usuarios_online_json(request):
    users = get_user_model().objects.all()
    online_users = [
        {"id": user.id, "username": user.username}
        for user in users
        if cache.get(f"user_online_{user.id}")
    ]
    return JsonResponse({"online_users": online_users})

# JSON ---- perguntas e respostas --------------------------------->
json_path = os.path.join(settings.BASE_DIR, 'JSON', 'faq.json')
with open(json_path, 'r', encoding='utf-8') as f:
    perguntas_respostas = json.load(f)

def encontrar_resposta(pergunta_user):
    pergunta_user = pergunta_user.lower()
    for categoria, perguntas in perguntas_respostas.items():
        for item in perguntas:
            if pergunta_user in item["pergunta"].lower():
                return item.get("resposta") or item.get("respostas")
    return "Desculpe, não entendi sua pergunta. Tente reformular ou acesse o menu de ajuda."


@login_required
def autocomplete_perguntas(request):
    perguntas = []

    for categoria, lista in perguntas_respostas.items():
        for item in lista:
            perguntas.append(item["pergunta"])

    return JsonResponse(perguntas, safe=False)


@login_required
@csrf_exempt
def limpar_chat(request):
    if 'chat_history' in request.session:
        del request.session['chat_history']
    return redirect('bot_chat')


@login_required
@csrf_exempt
def faq_view(request):
    if request.method == 'POST':
        texto = request.POST.get('text', '')
        resposta = encontrar_resposta(texto)
        
        historico = request.session.get('chat_history', [])
        historico.append({'text': texto, 'is_bot': False})
        historico.append({'text': resposta, 'is_bot': True})
        request.session['chat_history'] = historico
    else:
        historico = request.session.get('chat_history', [])

    contexto = {
        'messages': historico,
        'perguntas_respostas': perguntas_respostas
    }
    return render(request, 'chatbot.html', contexto)



@login_required
def create_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChatRoomForm()
        
    contexto = {
        "form": form
    }
    return render(request, 'create_room.html', contexto)


@login_required
def chat_room(request, slug):
    room = get_object_or_404(ChatRoom, slug=slug)
    messages = PublicMessage.objects.filter(room=room).order_by('timestamp')[:200]
    rooms = ChatRoom.objects.all()
    
    contexto = {
        'room': room,
        'messages': messages,
        'rooms': rooms,
    }
    return render(request, 'room.html', contexto)
    

@login_required
def delete_chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    room.delete()
    return redirect('home')