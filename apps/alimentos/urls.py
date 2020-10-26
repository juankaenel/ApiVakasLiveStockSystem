from django.urls import path
from . import views

urlpatterns = [
    path('alimentos/',views.AlimentosList.as_view(),name="alimentos_list"),
    path('alimentos/<str:pk>',views.AlimentosDetail.as_view(),name="alimentos_detail"),
]

