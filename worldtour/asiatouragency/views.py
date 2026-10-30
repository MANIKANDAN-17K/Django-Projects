from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, tourists! Welcome to the Asia Tour Agency.")
def about(request):
    return HttpResponse("We are a leading travel agency specializing in tours across Asia.")
