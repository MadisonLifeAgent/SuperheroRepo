from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#import our class/model
from .models import Superhero
from django.urls import reverse


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

# adds a new superhero to database
def create(request):
    if request.method == "POST":
        #grabs input from form fields
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superpower = request.POST.get('primary_superpower')
        secondary_superpower = request.POST.get('secondary_superpower')
        catchphrase = request.POST.get('catchphrase')

        #input is used to create and save a new superhero in to database
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_superpower=primary_superpower, secondary_superpower=secondary_superpower, catchphrase=catchphrase)
        new_superhero.save()

        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

# deletes a super hero from superhero database
def delete(request, superhero):
    superhero = Superhero.objects.get(id = superhero)
    context = {
        'superhero': superhero
    }
    #helps sends query results to template for display
    return render(request, 'superheroes/delete.html', context)
    
    if request.method == "POST":
        #gets input from user and checks it
        response = request.POST.get('response')

        if response == "yes":
            superhero.delete()

        return HttpResponseRedirect(reverse('superheroes:index'))

    else:
        return render(request, 'superheroes/indext.html')

