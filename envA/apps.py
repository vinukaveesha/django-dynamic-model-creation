from django.apps import AppConfig

class EnvaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'envA'

    def ready(self):
        from .models import create_all_dynamic_models

        db_configs = ['postgresql']

        for db_alias in db_configs:
            create_all_dynamic_models(db_alias)
