from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apps.alimentaciones.urls')),
    path('api/',include('apps.alimentos.urls')),
    path('api/',include('apps.jefes.urls')),
    path('api/auth/',include('apps.users.urls')),
]
