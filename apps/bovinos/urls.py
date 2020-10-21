from django.urls import path
from . import views

urlpatterns = [
    path('bovinos/',views.BovinosList.as_view(),name="bovinos_list"),
    path('bovinos/<str:pk>',views.BovinosDetail.as_view(),name="bovinos_detail"),
]

