from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("class/", views.Class, name="Class"),
path("journal", views.journal, name="journal")
]
#path names can be changed