from sys import setswitchinterval
from django.shortcuts import render
from .models import Employee
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings

import os

from .forms import EmployeeForm  # importați formularul corespunzător

from .static.formular.python.graphScripts import create_employee_graphs

def home(request):
    
    if request.method == 'POST' :
        
        form = EmployeeForm(request.POST)
        if form.is_valid():  # verificați dacă formularul este valid
            
            # Store info from the form
            nume = form.cleaned_data['firstname']
            prenume = form.cleaned_data['lastname']
            gender = form.cleaned_data['gender']
            jobTitle = form.cleaned_data['jobCategories']

            # Create a new Employee instance and save it to the database
            employee = Employee(
                first_name=nume,
                last_name=prenume,
                gender=gender,
                job_category=jobTitle
            )
            employee.save()

            messages.success(request, ("Added {} {} as {}! ").format(nume, prenume, jobTitle, gender))

            return redirect('home')
    else:
        form = EmployeeForm()

    return render(request, '../templates/formular/home.html',{"form": form})
    

def showTableDB(request):
    # Initialized a variable that stores all data from imported model
    employes = Employee.objects.all()

    # Create a list of tuples, with each tuple containing an index number (i+1) and an employee object
    projects_with_numbers = [(i+1, obj) for i, obj in enumerate(employes)]

    # Render the 'tableVisualization.html' template with the employes data passed as context
    return render(request, '../templates/formular/tableVisualization.html', {"employes" : projects_with_numbers})

def graphs(request):

    # Calea către directorul unde vor fi salvate graficele
    graphs_dir = os.path.join(settings.MEDIA_ROOT, 'formular', 'graphs')

    # Verifică dacă directorul există, altfel îl creează
    if not os.path.exists(graphs_dir):
        os.makedirs(graphs_dir)

    # Calea și numele fișierului pentru graficul pie
    pie_chart_path = os.path.join(graphs_dir, 'pie_chart.png')

    # Calea și numele fișierului pentru histograma joburilor
    histogram_path = os.path.join(graphs_dir, 'job_histogram.png')

    # Apelarea funcției create_employee_graphs pentru a genera graficele
    create_employee_graphs(Employee, pie_chart_path, histogram_path)

    
    return render(request, '../templates/formular/showGraphs.html')

def delete_employee(request, employee_id):

    # Get the Employee object with the given employee_id, or return a 404 page if it doesn't exist
    employee = get_object_or_404(Employee, id=employee_id)

    # Delete the employee from the database
    employee.delete()
    
    # Redirect to the page displaying the updated table
    return redirect('showTableDB')  # Redirecționează către pagina cu tabelul actualizat

