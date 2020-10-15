from django.urls import path, include
from . import views
#from rest_framework import routers
#from .views import AlimentacionesViewSet

#define la ruta para los modelos, get,post,put,delet,etc
#router = routers.DefaultRouter()
#router.register(r'',AlimentacionesViewSet)
#
#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('',views.apiOverView,name=""),
    path('alimentaciones/',views.index,name="index")

]