from django.urls import path
from .views import dynamic_model_view

urlpatterns = [
    path('dynamic/<str:app_label>/<str:model_name>/', dynamic_model_view, name='dynamic_model_view'),
]
