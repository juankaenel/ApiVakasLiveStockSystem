from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/login',views.UsuarioLoginAPIView.as_view(),name='login')
]