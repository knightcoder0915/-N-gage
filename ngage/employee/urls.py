from .import views
from django.urls import path

urlpatterns = [
    path('', views.hiit, name= 'hiit'),
    path('<int:pk>/', views.video, name='video'),
]