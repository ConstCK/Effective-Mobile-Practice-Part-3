from rest_framework import serializers

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Breed
