from django.apps import AppConfig


class FuriaChatappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Furia_chatapp'

    def ready(self):
        import Furia_chatapp.signals 