from django.urls import path
from .views import generate_name_view

urlpatterns = [
    path('', generate_name_view, name='generate_name'),
]
