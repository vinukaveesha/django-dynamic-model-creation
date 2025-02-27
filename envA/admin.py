from django.contrib import admin
from django.db import models
from django.conf import settings

def get_database_for_model(model):
    """
    Determines the database to use for a given model based on the database engine.
    """
    db_alias = 'default'
    try:
        engine = settings.DATABASES[db_alias]['ENGINE']
        if 'oracle' in engine:
            return 'oracle'
        else:
            return 'default'
    except KeyError:
        return 'default'

def register_dynamic_model(model):
    class DynamicAdmin(admin.ModelAdmin):
        def get_queryset(self, request):
            db_alias = get_database_for_model(self.model)
            return super().get_queryset(request).using(db_alias)
        
        list_display = [field.name for field in model._meta.fields if hasattr(field, 'name')]
        search_fields = [field.name for field in model._meta.fields if isinstance(field, models.CharField) and hasattr(field, 'name')]
        list_filter = [field.name for field in model._meta.fields if isinstance(field, models.BooleanField) and hasattr(field, 'name')]

    admin.site.register(model, DynamicAdmin)
