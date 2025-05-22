from django.urls import path
from .views import generate_bankaccount_view

urlpatterns = [
    path('', generate_bankaccount_view, name='generate_bankaccount'),
]
