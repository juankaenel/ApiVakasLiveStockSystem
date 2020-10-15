from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView,name=""),
    path('alimentaciones/',views.alimentacion_is,name="alimentacion_is"),
    path('alimentaciones/<str:pk>',views.alimentacion_sud,name="alimentacion_sud"),
]

