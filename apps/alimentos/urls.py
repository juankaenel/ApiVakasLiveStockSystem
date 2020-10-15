from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView,name=""),
    path('alimentos/',views.alimento_is,name="alimento_is"),
    path('alimentos/<str:pk>',views.alimento_sud,name="alimento_sud"),
]

