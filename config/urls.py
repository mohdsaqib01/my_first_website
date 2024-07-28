# URL configuration for config project.

# The urlpatterns list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import (index,login_view, 
                        register_view, logout_view,
                         add_task, complete_task, movies_view,
                           movie_add_view,movie_edit_view,
                           movie_delete_view, movie_search_view,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("_reload_/", include("django_browser_reload.urls")),
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path('logout', logout_view, name='logout'),
    path('add/', add_task, name='add_task'),
    path('complete/<int:id>/', complete_task, name='complete'),
    #crud operations
    path('movies/view', movies_view, name='view_movie'),
    path('movies/add', movie_add_view, name='add_movie'),
    path('movies/edit/<int:id>/', movie_edit_view, name='edit_movie'),
    path('movies/delete/<int:id>/', movie_delete_view, name='delete_movie'),
    path('movies/search', movie_search_view, name='search_movie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)