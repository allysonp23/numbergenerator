from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from numbergenerator.kafka_utils import KafkaTaskProducer, get_task_result


@swagger_auto_schema(method='post',
    operation_description="Envia solicitação de CPF para fila Kafka",
    manual_parameters=[
        openapi.Parameter('mask', openapi.IN_QUERY, description="Máscara? true/false", type=openapi.TYPE_BOOLEAN)
    ],
    responses={202: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'task_id': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['POST'])
def generate_cpf_view(request):
    """Endpoint para enviar geração de CPF para fila Kafka."""
    producer = KafkaTaskProducer()
    task_id = producer.send_task('generate_cpf', {'mask': request.GET.get('mask')})
    return Response({'task_id': task_id}, status=202)


@swagger_auto_schema(method='post',
    operation_description="Envia solicitação de CNPJ para fila Kafka",
    manual_parameters=[
        openapi.Parameter('mask', openapi.IN_QUERY, description="Máscara? true/false", type=openapi.TYPE_BOOLEAN)
    ],
    responses={202: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'task_id': openapi.Schema(type=openapi.TYPE_STRING)}
    )}
)
@api_view(['POST'])
def generate_cnpj_view(request):
    """Endpoint para enviar geração de CNPJ para fila Kafka."""
    producer = KafkaTaskProducer()
    task_id = producer.send_task('generate_cnpj', {'mask': request.GET.get('mask')})
    return Response({'task_id': task_id}, status=202)


@swagger_auto_schema(method='get',
    operation_description="Consulta resultado de uma tarefa pelo task_id",
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'result': openapi.Schema(type=openapi.TYPE_OBJECT)
            }
        ),
        404: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
        )
    }
)
@api_view(['GET'])
def get_task_status(request, task_id):
    """Endpoint para consultar status e resultado de uma tarefa."""
    result = get_task_result(task_id)
    if result:
        return Response(result)
    return Response({'error': 'Task not found'}, status=404)
