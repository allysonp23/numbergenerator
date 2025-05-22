from django.urls import path
from .views import generate_cpf_view, generate_cnpj_view

urlpatterns = [
    path('cpf/', generate_cpf_view, name='generate_cpf'),
    path('cnpj/', generate_cnpj_view, name='generate_cnpj'),
]
