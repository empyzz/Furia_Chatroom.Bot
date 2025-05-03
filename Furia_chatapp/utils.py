from django.contrib.auth import get_user_model
from django.core.cache import cache

def get_online_users():
    User = get_user_model()
    online_users = []
    for user in User.objects.all():
        if cache.get(f"user_online_{user.id}"):
            online_users.append(user)
    return online_users