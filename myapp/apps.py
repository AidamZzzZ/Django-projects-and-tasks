from django.apps import AppConfig

#es para configurar la aplicacion,es cm un settings pero solo para esta app

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
