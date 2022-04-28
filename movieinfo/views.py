from django.shortcuts import render
from .models import Movie

def info(request):
    data = Movie.objects.all()
    return render(request, 'movieinfo/info.html', context={'data':data})