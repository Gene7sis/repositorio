from django.db import models

# Create your models here.

#creacion de la tabla llamada Project que tendra una columna llamada name de un max de 200 carcateres
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title 

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
