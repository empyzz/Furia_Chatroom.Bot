from django.contrib import admin
from .models import *

# Registro do CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_seen', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-last_seen',)


# Registro do PublicMessage
class PublicMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'content')
    search_fields = ('user__username', 'content')
    ordering = ('-timestamp',)


# Registro do ChatRoom
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'theme')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

# Registrando os modelos no Django Admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PublicMessage, PublicMessageAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)