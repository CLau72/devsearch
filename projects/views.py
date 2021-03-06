from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'E-commerce Website',
        'description': 'Fully functional E-commerce site'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Website containing a portfolio of projects'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source social network'
    }
]

def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print('projectObj:', projectObj)
    return render(request, "projects/single-project.html", {"project": projectObj})
