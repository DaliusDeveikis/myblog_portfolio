from django.shortcuts import render

from .models import Project


def home(request):
    projects = Project.objects.order_by('-date')
    return render(request, 'portfolio/home.html', {'projects': projects})
