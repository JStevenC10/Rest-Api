from django.contrib.auth.models import User

from rest_framework import serializers
from .models import CinemaStudio, Gender, Movie

# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
    
    # HASH PASSWORD WITH SERIALIZER
    def create(self, validated_data):
        user =  super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

# CINEMA SERIALIZER
class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaStudio
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'Cinema Studio name': instance.name,
            'Logo': instance.logo.url if instance.logo else 'Logo not available'
        }

# GENDER SERIALIZER
class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('name',)

# MOVIE LIST ALL SERIALIZER
class MovieListserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'image', 'release_date', 'gender')

# MOVIE CREATE SERIALIZER
class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('state',)