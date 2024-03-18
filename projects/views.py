from django.shortcuts import render, HttpResponse

from .models import Project

def project_list(request):
    return render(request, "projects/project_list.html", {"projects": Project.objects.all()})

# The page shows all data of the project
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "projects/project_detail.html", {"project": project})

def project_create(request):
    return render(request, "projects/project_create.html")