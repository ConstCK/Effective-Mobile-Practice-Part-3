from django.utils.translation import gettext_lazy as _
from django.db import models


class DogGender(models.TextChoices):
    MALE = 'MALE', _('Самец')
    FEMALE = 'FEMALE', _('Самка')


class BreedSize(models.TextChoices):
    TINY = 'TINY', _('Крошечная')
    SMALL = 'SMALL', _('Маленькая')
    MEDIUM = 'MEDIUM', _('Средняя')
    LARGE = 'LARGE', _('Большая')
