from django.urls import path
from . import views

urlpatterns = [
    path('jefes/',views.JefesList.as_view(),name="jefes_list"),
    path('jefes/<str:pk>',views.JefesDetail.as_view(),name="jefes_detail"),
]

