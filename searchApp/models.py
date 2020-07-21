from django.db import models
from django.conf import settings

# Create your models here.
class Search(models.Model):
    name = models.CharField('Event Name', max_length=120)
    id = models.IntegerField(primary_key=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
