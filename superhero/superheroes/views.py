from django.shortcuts import render
from django.http import HttpResponse
#import our class/model
from .models import Superhero


# Create your views here.
# index page function that queries db for all superheroes and returns dictionary to template
def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    #sends the query result(s) to urls.py for display (or to the template)
    return render(request, 'superheroes/index.html', context)

# queries db for details about each superhero
def detail(request, superhero):
    superhero = Superhero.objects.get(id = superhero)
    context = {
        'superhero': superhero
    }
    #helps sends query results to template for display
    return render(request, 'superheroes/detail.html', context)