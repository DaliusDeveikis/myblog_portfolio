from django.shortcuts import render

from .models import About

def about(request):
    abouts = About.objects.all()
    print(abouts)
    return render(request, 'aboutme/about.html', {'abouts': abouts})
