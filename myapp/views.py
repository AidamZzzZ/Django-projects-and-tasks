from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import Create_new_task, Create_new_projects

# crear vistas para el usuario(por lo general html)


def index(request):
    title = "Django course!!"
    return render(request, "index.html", {"title": title})

def hello(request, username):
    return HttpResponse("<h2>Hello %s </h2>" % username)


def about(request):
    username = "adrian"
    return render(request, "about.html", {"username": username})


def projects(request):
    # mostrar una lista de valores del modelo project (todos los valores guardados hasta el momento)
    # project = list(Project.objects.values())
    project = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": project})


# aqui se puden hacer consultas,pasadno los parametros por url
def tasks(request):
    # se crea una variable donde se utiliza la funcion,get_object_or_404,se llama al formulario y cm parametro que llse llame al mismo titulo
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": Create_new_task()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            descripcion=request.POST["descripcion"],
            project_id=2,
        )
        return redirect("tasks")


def create_projects(request):
    if request.method == "GET":
        return render(request, "projects/create_projects.html", {
                'form': Create_new_projects()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
        
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project':project,
        'tasks': tasks
    })