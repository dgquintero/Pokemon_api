# Pokemon_api

In this repo I'm going to use the Pokemon API, where you can find a lot of information about pokemons. 

Here is the API documentation https://pokeapi.co/docs/v2 

## Use of this repo

First of all you have to clone the repository and install all the dependencies shown below.

After having all the dependencies installed you are ready to run the following API and be able to search for relevant information about your favorite pokemon.

``````
$ python manage.py runserver
``````

Now go to localhost:8000

## Set up Django
To create a Django app or to use the code from this repo, we will need to install Django.

First, though, consider creating a new virtual environment for your project so you can manage your dependencies separately.

``````

$ python3 -m venv env_pokeapi

``````

Now, we can install Django: 

``````
$ pip install django
``````

and, install Django REST Framework

``````
$ pip install djangorestframework
``````
