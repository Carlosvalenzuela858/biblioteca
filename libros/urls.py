from django.urls import path
from .views import autor_list_create, autor_detail, genero_detail, genero_list_create, calificacion_detail, calificacion_list_create, libro_detail, libro_list_create

urlpatterns = [
    path('autores/', autor_list_create),
    path('autores/<int:pk>/', autor_detail),
    
    path('generos/', genero_list_create),
    path('generos/<int:pk>/', genero_detail),
    
    path('calificaciones/', calificacion_list_create),
    path('calificaciones/<int:pk>/', calificacion_detail),
    
    path('libros/', libro_list_create),
    path('libros/<int:pk>/', libro_detail),  
]
