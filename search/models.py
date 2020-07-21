from django.db import models

# Create your models here.
class Search(models.Model):
    name = models.CharField('Event Name', max_length=120)
    id = models.IntegerField(primary_key=True)
    Base_stats = models.CharField(max_length=60)
    Height = models.IntegerField()
    weight = models.IntegerField()
    #Evolutions =
