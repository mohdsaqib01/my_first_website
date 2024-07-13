# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
     path("__reload__/", include("django_browser_reload.urls")),
     #home page
     path("", index, name="index")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)