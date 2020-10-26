from django.urls import path
from . import views

urlpatterns = [
    #path('usuarios/login',views.LoginUsuario,name='login'),
    #path('usuarios/registro',views.RegistroUsuario.as_view(),name='registro'),
    #path('usuarios/verificar-email',views.VerificarEmail.as_view(),name='verificar-email'),
    #path('usuarios/login',views.LoginAPIView.as_view(),name='login')
]

#Para probar las vistas podemos usar la libreria httpie -> pip install httpie
#http POST localhost:8000/api/usuarios/login -b
#http POST localhost:8000/api/usuarios/signup -b
#http POST localhost:8000/api/usuarios/signup email="juan@gmail.com" -b

