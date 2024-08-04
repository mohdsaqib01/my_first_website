from django import forms
from .models import Task, Movie
class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields =['name']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__' # double underscore with all calls all the fields(it will include all the fields of movie)
