from django import forms

class Create_new_task(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class' : 'input'}))
    descripcion = forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class':'input'}))
    
class Create_new_projects(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=200, widget=forms.TextInput(attrs={'class':'input'}))