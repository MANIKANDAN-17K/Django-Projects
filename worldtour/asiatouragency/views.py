from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tour
from .form import ContactForm 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .register import RegisterForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, tourists! Welcome to the Asia Tour Agency.")
def about(request):
    return HttpResponse("We are a leading travel agency specializing in tours across Asia.")
def schedule(request):
    data = Tour.objects.all()
    context = {'tours': data}
    return render(request, 'tour/schedule.html', context)
def imageviewer(request):
    return render(request, 'tour/imageviewer.html')

def home(request):
    return render(request, 'tour/home.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'tour/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'tour/contact_success.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid username or password."
            return render(request, 'accounts/login.html', {'error_message': error_message})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('home')

@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        return render(request, 'registration/protected.html')

 