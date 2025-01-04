from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Avg, Max, Subquery, OuterRef, F, Sum
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from .utils import DogsMixin


class DogViewSet(viewsets.ModelViewSet, DogsMixin):
    """Набор представлений для CRUD запросов к объектам Dog"""
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    def list(self, request, *args, **kwargs):
        # Получение списка всех собак из БД с дополнительными данными
        queryset = Dog.objects.all()
        # breeds = Breed.objects.annotate(avg_age=Avg('dogs__age')).values('avg_age', 'dogs__id')
        # breeds = Breed.objects.filter(id=OuterRef('dogs__breed'))
        # dogs = Dog.objects.filter(breed=OuterRef('breed')).values('age')
        #
        # q = Dog.objects.annotate(avg_age=Avg(Subquery(dogs), output_field=models.FloatField()))
        # for i in q:
        #     print(i.name, i.avg_age, i.breed)

        serializer = DogSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # Получение собаки с указанным id из БД с дополнительными данными

        try:
            dog = Dog.objects.get(id=kwargs.get('pk'))
            serializer = DogSerializer(dog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404({'error': f'Животное с указанным id={kwargs.get('pk')} не найдено.'})

    def create(self, request, *args, **kwargs):
        # Создание объекта собака в БД
        try:
            serializer = DogSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': f'Успешное создание объекта: {serializer.data}'},
                            status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({'error': f'Ошибка создания объекта: {error}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Удаление объекта собака с указанным id в БД
        try:
            dog = Dog.objects.get(id=kwargs.get('pk'))
            dog.delete()
            return Response({'message': f'Животное с id={kwargs.get('pk')} было удалено'},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            raise Http404(f'Животное с указанным id={kwargs.get('pk')} не найдено.')

    def update(self, request, *args, **kwargs):
        # Обновление объекта собака с указанным id в БД

        try:
            dog = Dog.objects.get(id=kwargs.get('pk'))
            dog_data = request.data.copy()
            serializer = DogSerializer(instance=dog, data=dog_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': f'Успешное обновление объекта: {serializer.data}'},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Некорректные данные о питомце'},
                                status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            raise Http404(f'Животное с указанным id={kwargs.get('pk')} не найдено.')


class BreedViewSet(viewsets.ModelViewSet):
    """Набор представлений для CRUD запросов к объектам Breed"""
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

    def list(self, request, *args, **kwargs):
        # Получение списка всех пород собак из БД с дополнительными данными
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # Получение породы собак с указанным id из БД с дополнительными данными
        try:
            breed = Breed.objects.get(id=kwargs.get('pk'))
            serializer = DogSerializer(breed)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404({'error': f'Порода собак с указанным id={kwargs.get('pk')} не найдена.'})

    def create(self, request, *args, **kwargs):
        # Создание объекта порода собаки в БД
        try:
            serializer = BreedSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': f'Успешное создание объекта: {serializer.data}'},
                            status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({'error': f'Ошибка создания объекта: {error}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Удаление объекта порода собаки с указанным id в БД
        try:
            breed = Breed.objects.get(id=kwargs.get('pk'))
            breed.delete()
            return Response({'message': f'Порода собак с id={kwargs.get('pk')} была удалена'},
                            status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404(f'Порода собак с указанным id={kwargs.get('pk')} не найдена.')

    def update(self, request, *args, **kwargs):
        # Обновление объекта порода собаки с указанным id в БД
        try:
            breed = Breed.objects.get(id=kwargs.get('pk'))
            breed_data = request.data.copy()
            serializer = BreedSerializer(instance=breed, data=breed_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': f'Успешное обновление объекта: {serializer.data}'},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Некорректные данные о породе собак'},
                                status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise Http404(f'Порода собак с указанным id={kwargs.get('pk')} не найдена.')
