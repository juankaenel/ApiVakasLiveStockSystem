from django.urls import path
from . import views

urlpatterns = [
    path('vacunas/',views.VacunasList.as_view(),name="vacunas_list"),
    path('vacunas/<str:pk>',views.VacunasDetail.as_view(),name="vacunas_detail"),
]

