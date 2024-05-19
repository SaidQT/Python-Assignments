from django.shortcuts import render
from . models import Movie,Actor,Director,Category
def index(request):
    context={
        "director":Director.objects.all,
        "Movie":Movie.objects.all,
        "Category": Category.objects.all,
        "actor":Actor.objects.all,
    }
    
    return render(request,"index.html", context)