from django.contrib import admin
from django.db import models
from django.conf import settings

def get_database_for_model(model):
    if 'public' in model._meta.db_table:
        return 'postgresql'
    else:
        return 'oracle'

def register_dynamic_model(model):
    class DynamicAdmin(admin.ModelAdmin):
        def get_queryset(self, request):
            db_alias = get_database_for_model(self.model)
            return super().get_queryset(request).using(db_alias)

        list_display = [field.name for field in model._meta.fields if hasattr(field, 'name')]
        search_fields = [field.name for field in model._meta.fields if isinstance(field, models.CharField) and hasattr(field, 'name')]
        list_filter = [field.name for field in model._meta.fields if isinstance(field, models.BooleanField) and hasattr(field, 'name')]

    admin.site.register(model, DynamicAdmin)
