from rest_framework import serializers
from .models import List, Users
from django.contrib.auth.hashers import make_password


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email', 'id', )

    

    