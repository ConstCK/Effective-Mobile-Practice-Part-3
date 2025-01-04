from rest_framework import serializers

from .constants import DogGender
from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
    average_age = serializers.DecimalField(max_digits=4, decimal_places=2, read_only=True)
    id = serializers.IntegerField(read_only=True)
    gender = serializers.ChoiceField(choices=DogGender, write_only=True)
    readable_gender = serializers.ChoiceField(source='get_gender_display',
                                              choices=DogGender.labels,
                                              read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'gender', 'color', 'favourite_food', 'favourite_toy', 'breed', 'average_age',
                  'readable_gender']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs']
