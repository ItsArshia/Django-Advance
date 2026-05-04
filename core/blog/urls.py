from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('about', views.indexView, name="fbv-text"),
    path('', TemplateView.as_view(template_name='index.html', extra_context={'name': 'arshia falahi'}))
]