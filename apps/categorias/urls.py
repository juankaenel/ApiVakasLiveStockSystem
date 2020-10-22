from django.urls import path
from . import views

urlpatterns = [
    path('categorias/',views.CategoriasList.as_view(),name="categorias_list"),
    path('categorias/<str:pk>',views.CategoriasDetail.as_view(),name="categorias_detail"),
]

