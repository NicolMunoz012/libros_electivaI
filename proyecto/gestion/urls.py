from django.urls import path
from .views import (
    AutorListView, AutorDeleteView, autor_create, autor_update,
    LibroListView, LibroDeleteView, libro_create, libro_update 
)

urlpatterns = [

    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/crear/', autor_create, name='autor_create'),
    path('autores/editar/<int:pk>/', autor_update, name='autor_update'),
    path('autores/eliminar/<int:pk>/', AutorDeleteView.as_view(), name='autor_delete'),

    path('libros/', LibroListView.as_view(), name='libro_list'),
    path('libros/crear/', libro_create, name='libro_create'),
    path('libros/editar/<int:pk>/', libro_update, name='libro_update'),
    path('libros/eliminar/<int:pk>/', LibroDeleteView.as_view(), name='libro_delete'),
]