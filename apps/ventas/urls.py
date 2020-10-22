from django.urls import path
from . import views

urlpatterns = [
    path('ventas/',views.VentasList.as_view(),name="ventas_list"),
    path('ventas/<str:pk>',views.VentasDetail.as_view(),name="ventas_detail"),
]

