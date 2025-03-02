from django.apps import AppConfig

class EnvaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'envA'

    def ready(self):
        from .models import create_dynamic_model, create_all_dynamic_models

        db_configs = {
            'postgresql': ['empi']
            # 'oracle': ['PH_PHARMACY']
        }

        for db_alias, schemas in db_configs.items():
            for schema in schemas:
                create_all_dynamic_models(db_alias, schema)