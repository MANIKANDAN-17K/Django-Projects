from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('schedule/', views.schedule),
    path('imageviewer/', views.imageviewer),
]