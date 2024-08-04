from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from .forms import TaskForm, MovieForm
from .models import Task, Movie

# for including databases

# Create your views here.

def index(request):
    task_list = Task.objects.all()#selects from task
    return render(request ,'index.html',{
        'tasks': task_list,
        'form': TaskForm()
    })
def add_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
def complete_task(request, id):
    task=Task.objects.get(id=id)#select *from where id =id
    task.completed= True 
    task.save()# update task set
    return redirect('index')   

def login_view(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request,'login.html')
def register_view(request):
    if request.method=='POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pwd')
        cpassword= request.POST.get('cpwd')
        print(username, email, password, cpassword)
        if password==cpassword:
            user=User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request,'register.html')
def logout_view(request):
    logout(request)
    return redirect('index')

def movie_view(request):
    movies = Movie.objects.all()
    return render(request, 'movies/view.html', {
        'movies':movies
    })
def movie_add_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_movies')
    return render(request,'movies/add.html',{'form':form}
                      )
    
def movie_edit_view(request, id):
    movie= Movie.objects.get(id=id)
    form = MovieForm(instance=movie)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('view_movies')
        return render(request,'movies/edit.html',{'form':form}
                      )
    
def movie_delete_view(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('view_movies')

def movie_search_view(request):
    return render(request,'movies/search.html')


    


