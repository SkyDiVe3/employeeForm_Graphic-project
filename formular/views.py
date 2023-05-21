from sys import setswitchinterval
from django.shortcuts import render
from .models import Project
from django.contrib import messages
from django.shortcuts import redirect

from .forms import EmployeeForm  # importați formularul corespunzător

def home(request):
    #Initialized a variable that stores all data from imported model
    
    if request.method == 'POST' :
        form = EmployeeForm(request.POST)
        if form.is_valid():  # verificați dacă formularul este valid
            # Store info from the form 
            # nume = request.POST.get("firstname")
            # prenume = request.POST.get("lastname")
            
            nume = form.cleaned_data['firstname']
            prenume = form.cleaned_data['lastname']
            gender = form.cleaned_data['gender']
            jobTitle = form.cleaned_data['jobCategories']

            messages.success(request, ("Added {} {} as {}, Gender = {}").format(nume, prenume, jobTitle, gender))
            return redirect('home')
    else:
        form = EmployeeForm()

    return render(request, '../templates/formular/home.html',{"form": form})
    

def showTableDB(request):
    projects  =  Project.objects.all()
    projects_with_numbers = [(i+1, obj) for i, obj in enumerate(projects)]
    return render(request, '../templates/formular/tableVisualization.html', {"projects" : projects_with_numbers})

