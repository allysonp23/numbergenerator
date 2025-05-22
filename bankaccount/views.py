from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .tasks import generate_bankaccount_task


@swagger_auto_schema(
    method='get',
    operation_description="Gera uma conta bancária fictícia",
    responses={200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'bank_account': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['GET'])
def generate_bankaccount_view(request):
    """Endpoint to generate a fictional bank account."""
    # Execute task and wait for result (sync mode)
    result = generate_bankaccount_task.delay().get()
    return Response({'bank_account': result})
