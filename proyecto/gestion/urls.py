from django.urls import path
from .views import AutorListView, AutorDeleteView, autor_create, autor_update

urlpatterns = [
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/crear/', autor_create, name='autor_create'),
    path('autores/editar/<int:pk>/', autor_update, name='autor_update'),
    path('autores/eliminar/<int:pk>/', AutorDeleteView.as_view(), name='autor_delete'),

]