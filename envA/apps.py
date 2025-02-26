# apps.py
from django.apps import AppConfig
import threading

class EnvaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'envA'

    def ready(self):
        from .models import create_dynamic_model

        db_configs = {
            'default': ['public.vet_specialties']
            # 'oracle': ['PH_PHARMACY.BRAND_MAPPING_TRACKER']
        }

        for db_alias, tables in db_configs.items():
            for table in tables:
                try:
                    dynamic_model = create_dynamic_model(table, db_alias)
                    print("Model created :",dynamic_model.get_fields())
                except Exception as e:
                    print(f"Error creating model for {table} in {db_alias}: {e}")
