from django.urls import path
from . import views

urlpatterns = [
    path('razas/',views.RazasList.as_view(),name="razas_list"),
    path('razas/<str:pk>',views.RazasDetail.as_view(),name="razas_detail"),
]

