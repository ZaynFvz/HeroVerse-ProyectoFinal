from django.apps import AppConfig


class HeroverseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'heroverse'

    def ready(self):
        import heroverse.signals
