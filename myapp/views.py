from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task, Person
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import TaskForm, ProjectForm, PersonForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def index(request):
    title = 'Django'
    return render(request, 'index.html', {
        'title' : title
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>HOLA %s</h1>" % username)
    
def about(request):
    return render(request, 'about.html')

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    
    #return render(request, 'projects.html', {
     #   'projects': projects
    #})
    
    if request.method == 'GET':
        return render(request, 'projects.html', {
        'form': ProjectForm(),
        'projects': projects
        })
    
    else:
   
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
    
    #return JsonResponse(projects, safe=False)

def tasks(request):
    
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    #return render(request, 'tasks.html', {
     
    #   'tasks': tasks
    #})
    
    if request.method == 'GET':
        return render(request, 'tasks.html', {
        'form': TaskForm(),
        'tasks': tasks
        })
    
    else:
   
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
    
   

    #return HttpResponse('Tasks: %s' % task.title)

class edicionTarea(UpdateView):
    
    model = Task
    form_class = TaskForm
    
    template_name = "edicionTarea.html"
    
    success_url = reverse_lazy("tasklist")
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(edicionTarea,self).form_valid(form)

class edicionProyecto(UpdateView):
    
    model = Project
    form_class = ProjectForm
    
    template_name = "edicionProyecto.html"
    
    success_url = reverse_lazy("projectlist")
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(edicionProyecto,self).form_valid(form)
    


def persons(request):
    context = {}
    
    form = ProjectForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    context['form'] = form
    return render(request, 'persons.html', context)

def eliminarProyecto(request, id):
    projects = Project.objects.get(id=id)
    projects.delete()
    
    return redirect('/projects/')

def eliminarTarea(request, id):
    task = Task.objects.get(id=id)
    print(task)
    task.delete()
    
    return redirect('/tasks/')