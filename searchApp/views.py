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

from .models import Search
from rest_framework import generics
from .serializers import SearchSerializer

class SearchAPIView(generics.ListCreateAPIView): 
    ''' generic api view countries model '''
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

# request to the pokemon api with all information about the pokemon
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
#        with open('dapi_data.json', 'w') as f:
#            json.dump(res, f)
            
#    return render(request, 'search/index.html')


# the view for the pokemon api
#def index(request):
#    pokemon = []
#    if request.method == 'POST':
#        f = open('api_data.json',)
#        data = json.load(f)
#        #print(data)
#        f.close()
#        print(data)
#        #print(data[0].key)
#        print(request.POST['search'])
#           print(pokemon)
#        for key in data[0]:
#        #print(data["name" == "bulbasaur")
#    return render(request, 'search/index.html')
