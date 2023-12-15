from django.db import models

#Para crear clases/modelos de tablas de tipo SQL

class Project(models.Model):
    name = models.CharField(max_length=50)
    #metodo para mostrar el nombre o datos en la interfaz
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name