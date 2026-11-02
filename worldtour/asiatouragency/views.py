from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour
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