from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    #helps display index.html or homepage
    path('', views.index, name='index'),

    #helps display details of each superhero
    path('<int:superhero>/', views.detail, name='detail'),

    #helps display create page
    path('create/', views.create, name='new_superhero')
]