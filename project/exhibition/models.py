from django.core import validators
from django.db import models

from .constants import DogGender, BreedSize


class Breed(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Порода собаки')
    size = models.CharField(max_length=8, choices=BreedSize.choices,
                            verbose_name='Размер собаки')
    friendliness = models.PositiveSmallIntegerField(verbose_name='Дружелюбность собаки',
                                                    validators=[validators.MinValueValidator(1),
                                                                validators.MaxValueValidator(5)]
                                                    )
    trainability = models.PositiveSmallIntegerField(verbose_name='Способность к тренировкам',
                                                    validators=[validators.MinValueValidator(1),
                                                                validators.MaxValueValidator(5)]
                                                    )
    shedding_amount = models.PositiveSmallIntegerField(verbose_name='Интенсивность линьки',
                                                       validators=[validators.MinValueValidator(1),
                                                                   validators.MaxValueValidator(5)]
                                                       )
    exercise_needs = models.PositiveSmallIntegerField(verbose_name='Потребность в упражнениях',
                                                      validators=[validators.MinValueValidator(1),
                                                                  validators.MaxValueValidator(5)]
                                                      )

    def __str__(self) -> str:
        return f'Порода собак: {self.name}'

    class Meta:
        verbose_name = 'Порода собаки'
        verbose_name_plural = 'Породы собак'
        ordering = ('name',)


class Dog(models.Model):
    name = models.CharField(max_length=64, verbose_name='Кличка собаки')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст собаки')
    gender = models.CharField(max_length=8,
                              choices=DogGender.choices, verbose_name='Пол собаки')
    color = models.CharField(max_length=128, verbose_name='Окрас собаки')
    favourite_food = models.CharField(max_length=128, verbose_name='Любимая еда')
    favourite_toy = models.CharField(max_length=128, verbose_name='Любимая игрушка')
    breed = models.ForeignKey(Breed,
                              on_delete=models.CASCADE, verbose_name='Порода собаки',
                              related_name='dogs')

    def __str__(self) -> str:
        return f'Собака по кличке {self.name}'

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ('breed', 'id')
        constraints = (models.UniqueConstraint(fields=('name', 'age', 'breed', 'gender'),
                                               name='Unique dog',),)
