from django.urls import path
from . import views

urlpatterns = [
    path('alimentaciones/',views.AlimentacionesList.as_view(),name="alimentacion_list"),
    path('alimentaciones/<str:pk>',views.AlimentacionesDetail.as_view(),name="alimentacion_detail")
]

