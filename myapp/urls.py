from django.urls import path
from . import views
from .views import edicionTarea, edicionProyecto

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects, name = 'projectlist'),
    path('tasks/', views.tasks, name = 'tasklist'),
    path('persons/', views.persons),
    path('projects/eliminarProyecto/<id>', views.eliminarProyecto),
    path('tasks/eliminarTarea/<id>', views.eliminarTarea, name="eliminar"),
    #path('tasks/edicionTarea/', views.edicionTarea)
    path('tasks/<pk>/update', edicionTarea.as_view(), name="editar"),
    path('projects/<pk>/update', edicionProyecto.as_view(), name="editarProyecto")
] 