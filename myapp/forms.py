from django.forms import ModelForm
from myapp.models import Task, Project, Person

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
