from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Band, Project

def index(request):
    return render(request, "website/index.html")