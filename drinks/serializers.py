from rest_framework import serializers
from .models import Drinks,Users

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields=['id','name','description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=['id','name','email','age']


