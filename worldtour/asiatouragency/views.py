from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tour
from .form import ContactForm 
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