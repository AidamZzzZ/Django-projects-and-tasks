from django.urls import path
from . import views

#aqui estamos creando urls que esten vinculados a la pagina
urlpatterns = [
    #podemos ponerle nombres de urls para que sea mas facil de identificar
    path('', views.index, name= "index"),
    path('about/', views.about, name= "about"),
    #asi se crea un url para pasar un parametro de tipo string (tambien se puede crear de tipo int)
    path('hello/<str:username>', views.hello, name= "hello"),
    path('projects/', views.projects, name= "projects"),
    path('projects/<int:id>', views.project_detail, name= "project_detail"),
    path('tasks/', views.tasks, name= "tasks"),
    path('create_task/', views.create_task, name= "create_task"),
    path('create_projects/', views.create_projects, name= "create_projects"),    
]