from django.urls import path
from .views import generate_phone_view

urlpatterns = [
    path('', generate_phone_view, name='generate_phone'),
]
