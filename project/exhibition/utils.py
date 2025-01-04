from django.db.models import OuterRef, Avg, Subquery, Count

from .models import Dog, Breed


class SubqueryMixin:
    @staticmethod
    def get_average_age() -> Subquery:
        # Метод для получения среднего возраста собак для породы из внешнего запроса
        result = Subquery(
            Breed.objects.filter(id=OuterRef('breed'))
            .annotate(avg_age=Avg('dogs__age'))
            .values('avg_age')[:1]
            )
        return result

    @staticmethod
    def get_dogs_number_for_breed(breed_id: int) -> int:
        # Метод для получения количества собак для указанной породы
        result = Breed.objects.filter(id=breed_id).aggregate(number=Count('dogs__id'))
        return result['number']

    @staticmethod
    def get_dogs_number_for_all_breeds() -> Subquery:
        # Метод для получения количества собак для породы из внешнего запроса
        result = Subquery(Breed.objects.filter(id=OuterRef('id'))
                          .annotate(total_dogs=Count('dogs'))
                          .values('total_dogs')[:1]
                          )
        return result
