from django.urls import path, include
from rest_framework import routers
from .views import AlimentosViewSet

#define la ruta para los modelos, get,post,put,delet,etc
router = routers.DefaultRouter()
router.register(r'',AlimentosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]