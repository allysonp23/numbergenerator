from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Number Generator API",
        default_version='v1',
        description="API para gerar dados fictícios (CPF, CNPJ, nomes, telefones, lorem ipsum)",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cpf_cnpj.urls')),
    path('api/lorem/', include('lorem.urls')),
    path('api/phone/', include('phone.urls')),
    path('api/names/', include('names.urls')),
    path('auth/', include('authentication.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
