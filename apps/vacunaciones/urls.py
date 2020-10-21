from django.urls import path
from . import views

urlpatterns = [
    path('vacunaciones/',views.VacunacionesList.as_view(),name="vacunaciones_list"),
    path('vacunaciones/<str:pk>',views.VacunacionesDetail.as_view(),name="vacunaciones_detail"),
]

