from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 150)
    completed = models.BooleanField(default=False)
class Movie(models.Model):
    title = models.CharField(max_length = 150)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='movies')
        
    #1. python manage.py makemigrations
    #2.python manage.py migrate
        
        


