from django.shortcuts import render
from django.apps import apps
from django.http import Http404

def dynamic_model_view(request, app_label, model_name):
    # Try to get the model class from the app registry
    Model = apps.get_model(app_label, model_name)
    if not Model:
        raise Http404(f"Model {model_name} not found in app {app_label}")

    # Fetch data from the model
    objects = Model.objects.all()

    context = {
        'objects': objects,
        'model_name': model_name,
    }
    return render(request, 'dynamic_model_template.html', context)
