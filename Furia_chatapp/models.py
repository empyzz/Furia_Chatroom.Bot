from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify


class CustomUser(AbstractUser):
    last_seen = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


class ChatRoom(models.Model):
    THEME_CHOICES = [
        ('championships', 'Campeonatos e Torneios'),
        ('teams_players', 'Times e Jogadores'),
        ('stats_rankings', 'Estatísticas e Rankings'),
        ('updates_news', 'Atualizações e Notícias'),
        ('strategies', 'Estratégias e Táticas'),
        ('skins_items', 'Skins e Itens'),
        ('community_events', 'Comunidade e Eventos'),
        ('other', "Outros")
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    theme = models.CharField(max_length=50, choices=THEME_CHOICES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class PublicMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)