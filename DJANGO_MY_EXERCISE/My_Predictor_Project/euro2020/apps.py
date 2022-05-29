from django.apps import AppConfig


class Euro2020Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'euro2020'

    def ready(self):
        import euro2020.signals
