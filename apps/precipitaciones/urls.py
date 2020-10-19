from django.urls import path
from . import views

urlpatterns = [
    path('precipitaciones/',views.PrecipitacionesList.as_view(),name="precipitaciones_list"),
    path('precipitaciones/<str:pk>',views.PrecipitacionesDetail.as_view(),name="precipitaciones_detail"),
]

