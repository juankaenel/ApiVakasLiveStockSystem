from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/',include('apps.alimentaciones.urls')),
    path('api/',include('apps.alimentos.urls')),
    path('api/auth/',include('apps.users.urls')),
]