from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import UserRegistrationSerializer


@swagger_auto_schema(method='post',
    operation_description="Registrar novo usuário",
    request_body=UserRegistrationSerializer,
    responses={
        201: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING),
                'access': openapi.Schema(type=openapi.TYPE_STRING),
                'refresh': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        400: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
        )
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """Endpoint para registro de novos usuários."""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'User created successfully',
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
