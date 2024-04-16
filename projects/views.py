from django.shortcuts import render, HttpResponse, redirect

from .models import Project, Task, StatusChoices, PriorityChoices

def project_list(request):
    return render(request, "projects/project_list.html", {"projects": Project.objects.all()})

def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, "projects/project_detail.html", {"project": project})

def project_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        budget = request.POST.get('budget')
        owner = request.POST.get('owner')
        
        project = Project(title=title, description=description, deadline=deadline, status=status, priority=priority, budget=budget, owner=owner)
        project.save()
        return redirect('project_list')
    else:
        return render(request, 'projects/project_create.html', {
            'StatusChoices': StatusChoices,
            'PriorityChoices': PriorityChoices,
        })
        
def project_delete(request, id):
    if request.method == 'POST':
        project = Project.objects.get(pk=id)
        project.delete()
        return redirect('project_list')
    else:
        return render(request, 'projects/project_delete.html', {
            'projects': Project.objects.all(),
        })

def task_list(request):
    return render(request, "projects/task_list.html", {"tasks": Task.objects.all()})

def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "projects/task_detail.html", {"task": task})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        project = request.POST.get('project')
        
        task = Task(title=title, description=description, deadline=deadline, status=status, priority=priority, project_id=project)
        task.save()
        return redirect('task_list')
    else:
        return render(request, 'projects/task_create.html', {
            'StatusChoices': StatusChoices,
            'PriorityChoices': PriorityChoices,
            'projects': Project.objects.all(),
        })