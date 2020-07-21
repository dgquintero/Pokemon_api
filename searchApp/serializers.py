from rest_framework import serializers
from .models import Search

class SearchSerializer(serializers.ModelSerializer):
    '''serializer Search model'''
    class Meta:
        model = Search
        fields = "__all__"
