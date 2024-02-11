
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showsavailable
        fields = '__all__'


class BookedShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedShows
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']