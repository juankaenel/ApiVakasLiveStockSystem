from django.urls import path
from . import views

urlpatterns = [
    path('empleados/',views.EmpleadosList.as_view(),name="empleados_list"),
    path('empleados/<str:pk>',views.EmpleadosDetail.as_view(),name="empleados_detail"),
]

