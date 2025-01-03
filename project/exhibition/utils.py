from django.db.models import Avg

from .models import Dog


class DogsMixin:
    @staticmethod
    def get_average_age():
        result = Dog.objects.aggregate(Avg('age', default=0))
        return result
