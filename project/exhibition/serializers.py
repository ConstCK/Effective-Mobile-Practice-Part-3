from rest_framework import serializers

from .constants import DogGender, BreedSize
from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
    average_age = serializers.DecimalField(max_digits=4, decimal_places=2,
                                           read_only=True)
    number = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    gender = serializers.ChoiceField(choices=DogGender, write_only=True)
    readable_gender = serializers.ChoiceField(source='get_gender_display',
                                              choices=DogGender.labels,
                                              read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'gender', 'color', 'favourite_food',
                  'favourite_toy', 'breed', 'average_age', 'readable_gender',
                  'number']


class BreedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    size = serializers.ChoiceField(choices=BreedSize, write_only=True)
    readable_size = serializers.ChoiceField(source='get_size_display',
                                            choices=BreedSize.labels,
                                            read_only=True)
    total_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'readable_size', 'friendliness',
                  'trainability', 'shedding_amount', 'exercise_needs',
                  'total_dogs']
