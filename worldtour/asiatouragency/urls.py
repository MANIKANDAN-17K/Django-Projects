from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('schedule/', views.schedule),
    path('imageviewer/', views.imageviewer),
    path('contact/', views.contact, name='contact'),
    path('contact/success', views.contact_success_view, name='contact-success'),
    path('home/', views.home, name='home'),
]