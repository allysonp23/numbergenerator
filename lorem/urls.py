from django.urls import path
from .views import generate_lorem_view

urlpatterns = [
    path('', generate_lorem_view, name='generate_lorem'),
]
