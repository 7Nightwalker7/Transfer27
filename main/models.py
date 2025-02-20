from tkinter.constants import CASCADE

from django.db import models
from django.db.models import CharField, PositiveSmallIntegerField, ForeignKey, ImageField, DateField


class Country(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name


class Season(models.Model):
    name = CharField(max_length=64)
    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=64)
    coach = models.CharField(max_length=64)
    f_date = models.DateField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOISE = {
        'GK': 'GK',
        'SW': 'SW',
        'CB': 'CB',
        'RB': 'RB',
        'LB': 'LB',
        'RBW': 'RBW',
        'LBW': 'LBW',
        'DM': 'DM',
        'CM': 'CM',
        'SS': 'SS',
        'RW': 'RW',
        'LW': 'LW',
        'CF': 'CF',
    }
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=255,choices=POSITION_CHOISE)
    nation = models.ForeignKey(Country,on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class Transfer(models.Model):
    player_id = models.ForeignKey(Player,on_delete=models.CASCADE)
    club_from = models.ForeignKey(Club,on_delete=models.CASCADE,related_name='club_from',)
    club_to = models.ForeignKey(Club,on_delete=models.CASCADE,related_name='club_to',)
    season = models.ForeignKey(Season,on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    price_tft = models.PositiveSmallIntegerField()
    datetime = models.DateField()