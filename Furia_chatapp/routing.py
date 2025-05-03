from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<slug:slug>/', ChatConsumer.as_asgi()),
]
