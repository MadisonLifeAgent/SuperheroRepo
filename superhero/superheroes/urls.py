from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    #helps display index.html or homepage
    path('', views.index, name='index'),

    #helps display details of each superhero
    path('<int:superhero>/', views.detail, name='detail'),

    #helps display create page
    path('create/', views.create, name='new_superhero'),

    #helps display delete page
    path('<int:superhero>/delete/', views.delete, name='delete'),

    #helps display edit page
    path('<int:superhero>/edit/', views.edit, name='edit_superhero')
]