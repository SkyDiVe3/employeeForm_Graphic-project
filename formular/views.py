from django.shortcuts import render
from .models import Project
# Create your views here.

def home(request):
    projects  =  Project.objects.all()
    projects_with_numbers = [(i+1, obj) for i, obj in enumerate(projects)]

    return render(request, '../templates/formular/home.html', {"projects" : projects_with_numbers})