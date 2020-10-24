from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/login',views.UsuarioLoginAPIView.as_view(),name='login'),
    path('usuarios/signup',views.UsuarioSignUpAPIView.as_view(),name='signup')
]

#Para probar las vistas podemos usar la libreria httpie -> pip install httpie
#http POST localhost:8000/api/usuarios/login -b
#http POST localhost:8000/api/usuarios/signup -b
#http POST localhost:8000/api/usuarios/signup email="juan@gmail.com" -b

