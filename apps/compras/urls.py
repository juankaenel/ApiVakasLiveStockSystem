from django.urls import path
from . import views

urlpatterns = [
    path('compras/',views.ComprasList.as_view(),name="compras_list"),
    path('compras/<str:pk>',views.ComprasDetail.as_view(),name="compras_detail"),
]

