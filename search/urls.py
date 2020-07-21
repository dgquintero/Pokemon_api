from django.urls import path
from . import views
from .views import ListPokemon
from rest_framework import routers


urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/(?P<name>[0-20]+)$', ListPokemon.as_view(), name='detail-pokemon')
]
