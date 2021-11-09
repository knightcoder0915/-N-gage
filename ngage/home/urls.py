
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    #path("",home,name="home"),
    #path('',include('home.urls')),
]
