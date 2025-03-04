from django.urls import path
from .views import views
# from .views import carrera_views, curso_views, materia_views,

urlpatterns = [
    path('', views.inicio),
    path('carreras/', views.carreras, name="carreras"),
    path('crear_carrera/', views.crear_carrera, name="crear_carrera"),
    path('eliminar_carrera/<id>', views.eliminar_carrera, name="eliminar_carrera"),
    path('editar_carrera/<id>', views.editar_carrera, name="editar_carrera"),
    path('procesar_editar_carrera/', views.procesar_editar_carrera, name="procesar_editar_carrera"),
]
