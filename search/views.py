import requests
import os, json
from django.conf import settings
from django.shortcuts import render
from collections import ChainMap
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Search
from django.http import Http404

# request to the pokemon api with all information abou the pokemon
#def index(request):
#    res = []
#    for i in range(1, 806):
#        resu = {}
#        u = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
#        response = requests.get(u)
#        if response:
#            result = response.json()

#            resu.update({"id": i,
#                        "name": result['forms'][0]['name'],
#                        "height": result['height'],
#                        "weight": result['weight'],})
#    
#            for stat in result['stats']:
#                stats = {}

#               resu.update({stat['stat']['name']: stat['base_stat']})
#        res.append(resu)
#        with open('data.json', 'w') as f:
#            json.dump(res, f)
            
#    return render(request, 'search/index.html')


def index(request):
    pokemon = []
    if request.method == 'POST':
        f = open('api_data.json',)
        data = json.load(f)
        #print(data)
        print(request.POST['search'])
        for pokemon in data.key:
            print(pokemon)
        #print(data["name" == "bulbasaur")
    return render(request, 'search/index.html')

class ListPokemon(APIView):
    def get_object(self, name):
        try:
            return Search.objects.get(name=name)
        except Search.DoesNotExist:
            raise Http404

    def get(self, request, name):
        search = self.get_object(name)

        search_json = "pokemon_api/api_data.json"
        return Response(search_json.data)

class PokemonView(viewsets.ModelViewSet):
    search_json = "pokemon_api/api_data.json"

