from rest_framework import serializers
from .models import CinemaStudio, Gender, Movie

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