import matplotlib
matplotlib.use('Agg')  # Setare backend non-interactiv


import matplotlib.pyplot as plt
from django.db import models

def create_employee_graphs(Employee, pie_chart_path, histogram_path):
    print("----------------Crearea graficelor-----------------")
    # Obțineți toți angajații din modelul Employee
    employees = Employee.objects.all()

    # Calculează numărul de angajați pentru fiecare gen
    gender_counts = employees.values('gender').annotate(count=models.Count('id'))

    # Extrageți genurile și numerele corespunzătoare
    genders = [item['gender'] for item in gender_counts]
    counts = [item['count'] for item in gender_counts]

    # Culoare pentru fiecare gen
    colors = ['pink', 'blue', 'gold', 'green', 'orange']

    # Creați graficul pie pentru repartizarea pe genuri a angajaților
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=genders, colors=colors, autopct='%1.1f%%')
    plt.title('Repartiția pe genuri a angajaților')
    plt.axis('equal')
    plt.savefig(pie_chart_path, format='png')
    plt.close()

    # Obțineți lista categoriilor de joburi
    job_categories = Employee.objects.values_list('job_category', flat=True).distinct()
    # Calculează numărul de angajați pentru fiecare categorie de job
    job_counts = employees.values('job_category').annotate(count=models.Count('id'))

    # Extrageți categoriile de job și numerele corespunzătoare
    job_labels = [str(item['job_category']) for item in job_counts]
    job_counts = [item['count'] for item in job_counts]

    # Creați histograma pentru repartizarea joburilor de angajați
    plt.figure(figsize=(8, 6))
    plt.bar(job_labels, job_counts)
    plt.xlabel('Categorii de joburi')
    plt.ylabel('Număr de angajați')
    plt.title('Repartiția joburilor de angajați')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(histogram_path, format='png')
    plt.close()
    print("----------------Graficele au fost create!-----------------")