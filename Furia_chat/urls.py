from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Furia_chatapp.urls')),  # Rotas do app de chat
    path('accounts/', include('allauth.urls')),  # Rotas do allauth
    path('admin/', admin.site.urls),  # Rotas do admin
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    