from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')

def overview(request):
    return render(request, 'overview.html')

def phenology(request):
    return render(request, 'phenology.html')

def resources(request):
    return render(request, 'resources.html')
