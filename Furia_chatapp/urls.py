from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # A URL 'home' está definida aqui
    path('  ', views.create_room, name='create_room'),
    path('perfil/', views.profile, name='profile'),
    path('change_name/', views.change_name, name='change_name'),
    path('change_password/', views.change_password, name='change_password'),
    path('sala/<slug:slug>/', views.chat_room, name='chat_room'),
    path('chat/bot/', views.faq_view, name='bot_chat'),
    path('delete-room/<int:room_id>/', views.delete_chat_room, name='delete_chat_room'),
    path('autocomplete-perguntas/', views.autocomplete_perguntas, name='autocomplete_perguntas'),
    path('limpar-chat/', views.limpar_chat, name='limpar_chat'),
    path('usuarios_online_json/', views.lista_usuarios_online_json, name='usuarios_online_json'),
    path('upload_profile_image/', views.upload_profile_image, name="upload_profile_image")

]   