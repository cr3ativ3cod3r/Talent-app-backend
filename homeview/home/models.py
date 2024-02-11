from django.db import models
from django.contrib.auth.models import User
import datetime

 
class Item(models.Model):
    postno = models.PositiveIntegerField()
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length=100, null=True)
    tag = models.CharField(max_length = 400)
    content = models.CharField(max_length = 600)
    likes = models.PositiveIntegerField()
    upload = models.FileField(upload_to ='../uploads/', null=True) 
    time = models.TimeField(null=True)


    def __int__(self):
        return self.postno
    
class Shows(models.Model):
    showname = models.CharField(max_length = 25, null = True)

    
class Showsavailable(models.Model):
    showID = models.CharField(max_length = 25, null = True)
    showname = models.TextField(max_length = 100, null = True)
    place = models.TextField(null = True)
    time = models.TimeField(default = "00:00:00")
    seats_remaining = models.PositiveIntegerField(null = True)
    fundraiser = models.BooleanField(null=True)

    def __str__(self):
        return self.showname

class BookedShows(models.Model):
    #showID = models.ForeignKey(Showsavailable,on_delete = models.CASCADE, null = True)
    id_key = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    showname = models.TextField(max_length = 100, null = True)
    place = models.TextField(null = True)
    time = models.TimeField(default = "00:00:00")
    seats_remaining = models.PositiveIntegerField(null = True)
    fundraiser = models.BooleanField(null=True)

    def __str__(self):
        return self.showname
    
class Registermodel(models.Model):
    username = models.TextField(max_length = 100, null = True)
    password = models.TextField(max_length = 100, null = True)

class Loginmodel(models.Model):
    username = models.TextField(max_length = 100, null = True)
    password = models.TextField(max_length = 100, null = True)

