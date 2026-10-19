from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from .models import Project, Skill

def projects(request):
    return render(request, "portfolio/projects.html", {
        "projects": Project.objects.all(),
        "skills": Skill.objects.all(),
    })


def home(request):
    return render(request, "portfolio/index.html")


def about(request):
    return render(request, "portfolio/about.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def cv(request):
    return render(request, "portfolio/resume.html")


def contact(request):
    return render(request, "portfolio/contact.html")