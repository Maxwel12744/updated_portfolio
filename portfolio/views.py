
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
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
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Thanks for your message! I'll get back to you soon.")
            return redirect("contact")
    return render(request, "portfolio/contact.html")