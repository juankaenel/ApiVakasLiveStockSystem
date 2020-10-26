from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Bovinos API",
      default_version='v1',
      description="Test description",
      #terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="contact@snippets.local"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('apps.alimentaciones.urls')),
    path('api/v1/',include('apps.alimentos.urls')),
    #path('api/', include('apps.usuarios.urls')),
    path('api/v1/',include('apps.jefes.urls')),
    path('api/v1/',include('apps.empleados.urls')),
    path('api/v1/',include('apps.precipitaciones.urls')),
    path('api/v1/',include('apps.vacunas.urls')),
    path('api/v1/',include('apps.vacunaciones.urls')),
    path('api/v1/',include('apps.bovinos.urls')),
    path('api/v1/',include('apps.compras.urls')),
    path('api/v1/',include('apps.ventas.urls')),
    path('api/v1/',include('apps.categorias.urls')),
    path('api/v1/',include('apps.razas.urls')),
    #swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #rest_auth
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    #path('accounts/', include('allauth.urls')),
]

