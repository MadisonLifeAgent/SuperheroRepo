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

# queries db for details about a superhero
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

        # returns to index/home page
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        # displays add a new superhero form
        return render(request, 'superheroes/create.html')

# deletes a super hero from superhero database
def delete(request, superhero):
    superhero = Superhero.objects.get(id = superhero)
    
    # delete method
    superhero.delete()

    # return to index/home page
    return HttpResponseRedirect(reverse('superheroes:index'))

# edits a superhero in the database
def edit(request, superhero):
    # get form changes or values
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superpower = request.POST.get('primary_superpower')
        secondary_superpower = request.POST.get('secondary_superpower')
        catchphrase = request.POST.get('catchphrase')

        # save edits to superhero
        # make sure to add primary key id so it does not create a new row in the db
        edit_superhero = Superhero(id=superhero, name=name, alter_ego=alter_ego, primary_superpower=primary_superpower, secondary_superpower=secondary_superpower, catchphrase=catchphrase)

        edit_superhero.save()

        # return to home page
        return HttpResponseRedirect(reverse('superheroes:index'))

    else:
        # display the edit page with superhero details and form fields
        superhero = Superhero.objects.get(id = superhero)
        context = {
            'superhero': superhero
        }
        
        return render(request, 'superheroes/edit.html', context)
