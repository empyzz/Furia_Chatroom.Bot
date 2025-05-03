import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Furia_chat.settings')

import django
django_asgi_app = get_asgi_application()
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
from Furia_chatapp.routing import websocket_urlpatterns 

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

