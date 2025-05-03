from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_out)
def remover_usuario_do_cache(sender, request, user, **kwargs):
    if user.is_authenticated:
        cache.delete(f"user_online_{user.id}")