from django.contrib import admin
from django.db import models

def register_dynamic_model(model):
    class DynamicAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
        search_fields = [field.name for field in model._meta.fields if isinstance(field, models.CharField)]
        list_filter = [field.name for field in model._meta.fields if isinstance(field, models.BooleanField)]
    
    admin.site.register(model, DynamicAdmin)
