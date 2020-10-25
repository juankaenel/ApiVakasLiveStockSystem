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
    path('api/',include('apps.alimentaciones.urls')),
    path('api/',include('apps.alimentos.urls')),
    path('api/', include('apps.usuarios.urls')),
    path('api/',include('apps.jefes.urls')),
    path('api/',include('apps.empleados.urls')),
    path('api/',include('apps.precipitaciones.urls')),
    path('api/',include('apps.vacunas.urls')),
    path('api/',include('apps.vacunaciones.urls')),
    path('api/',include('apps.bovinos.urls')),
    path('api/',include('apps.compras.urls')),
    path('api/',include('apps.ventas.urls')),
    path('api/',include('apps.categorias.urls')),
    path('api/',include('apps.razas.urls')),
    #swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

