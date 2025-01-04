from django.db.models import Avg

from .models import Dog, Breed


class DogsMixin:
    @staticmethod
    def get_average_age(breed: int):
        result = Breed.objects.filter(id=breed)
        return result
