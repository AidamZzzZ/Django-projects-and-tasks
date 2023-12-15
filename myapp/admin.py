from django.contrib import admin
from .models import Project, Task

#es para añadir aplicaciones y administrar los modelos,se pueden crear datos o usuarios,etc...
#para añadirlo se hace de la siguiente manera
admin.site.register(Project)
admin.site.register(Task)

