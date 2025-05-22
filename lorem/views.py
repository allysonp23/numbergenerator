from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .utils import generate_lorem


@swagger_auto_schema(method='get',
    operation_description="Gera texto Lorem Ipsum de tamanho especificado",
    manual_parameters=[
        openapi.Parameter('length', openapi.IN_QUERY, description="Número de caracteres", type=openapi.TYPE_INTEGER)
    ],
    responses={200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'lorem': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['GET'])
def generate_lorem_view(request):
    """Endpoint para gerar texto Lorem Ipsum de tamanho especificado em caracteres."""
    length_param = request.GET.get('length')
    try:
        length = int(length_param) if length_param is not None else 0
    except (TypeError, ValueError):
        return Response({'error': 'length deve ser um inteiro'}, status=400)
    text = generate_lorem(length)
    return Response({'lorem': text})
