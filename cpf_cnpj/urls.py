from django.urls import path
from .views import generate_cpf_view, generate_cnpj_view, get_task_status

urlpatterns = [
    path('cpf/', generate_cpf_view, name='generate_cpf'),
    path('cnpj/', generate_cnpj_view, name='generate_cnpj'),
    path('tasks/<str:task_id>/', get_task_status, name='get_task_status'),
]
