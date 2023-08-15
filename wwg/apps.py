from django.apps import AppConfig


class WwgConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wwg'

    def ready(self):
        import wwg.signal