from django.apps import AppConfig


class InstitucionalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website.institucional'
    
    def ready(self):
        import website.institucional.signals  # importa os signals quando o app estiver pronto

