from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .utils import generate_phone


@swagger_auto_schema(method='get',
    operation_description="Gera um número de telefone fictício no formato DD 9 NNNN NNNN",
    responses={200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'phone': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['GET'])
def generate_phone_view(request):
    """Endpoint para gerar um telefone fictício brasileiro."""
    phone = generate_phone()
    return Response({'phone': phone})
