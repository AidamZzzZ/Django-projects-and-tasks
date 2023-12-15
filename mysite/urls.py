from django.contrib import admin
from django.urls import path, include

#aqui se importan las rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    #amedida de que se creen mas rutas,estas no se pueden repetir entre si
]
