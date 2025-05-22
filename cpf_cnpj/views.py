from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .utils import get_cpf, get_cnpj
from .tasks import generate_cpf_task, generate_cnpj_task


@swagger_auto_schema(method='get',
    operation_description="Gera um CPF fictício válido",
    manual_parameters=[
        openapi.Parameter('mask', openapi.IN_QUERY, description="Máscara? true/false", type=openapi.TYPE_BOOLEAN)
    ],
    responses={200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'cpf': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['GET'])
def generate_cpf_view(request):
    """Endpoint to generate a fictional CPF."""
    # Execute task and wait for result (sync mode)
    result = generate_cpf_task.delay(request.GET.get('mask')).get()
    return Response({'cpf': result})


@swagger_auto_schema(method='get',
    operation_description="Gera um CNPJ fictício válido",
    manual_parameters=[
        openapi.Parameter('mask', openapi.IN_QUERY, description="Máscara? true/false", type=openapi.TYPE_BOOLEAN)
    ],
    responses={200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'cnpj': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)

@api_view(['GET'])
def generate_cnpj_view(request):
    """Endpoint to generate a fictional CNPJ."""
    # Execute task and wait for result (sync mode)
    result = generate_cnpj_task.delay(request.GET.get('mask')).get()
    return Response({'cnpj': result})
