from django.conf.urls import url
from searchApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'pokemons', views.SearchAPIView.as_view(), name='pokemons-list')
]
