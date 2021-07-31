from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    #helps display index.html or homepage
    path('', views.index, name='index'),
    #helps display details of each superhero
    path('<int:superhero_id>/', views.detail, name='detail')
]