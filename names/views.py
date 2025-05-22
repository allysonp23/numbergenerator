from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .utils import generate_name


@swagger_auto_schema(method='get',
    operation_description="Gera um nome fictício português com dois sobrenomes distintos",
    manual_parameters=[
        openapi.Parameter('gender', openapi.IN_QUERY, description="Gênero: 'male' ou 'female' (opcional)", type=openapi.TYPE_STRING)
    ],
    responses={200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'name': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['GET'])
def generate_name_view(request):
    """Endpoint para gerar um nome fictício português."""
    gender = request.GET.get('gender')
    name = generate_name(gender=gender)
    return Response({'name': name})
