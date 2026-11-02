from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index),
    path('', views.home_view, name='home'),
    path('about/', views.about),
    path('schedule/', views.schedule),
    path('imageviewer/', views.imageviewer),
    path('contact/', views.contact, name='contact'),
    path('contact/success', views.contact_success_view, name='contact-success'),
    #path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    
]