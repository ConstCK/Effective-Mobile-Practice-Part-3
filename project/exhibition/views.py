from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Dog
from .serializers import DogSerializer
from .utils import DogsMixin


class DogViewSet(viewsets.ModelViewSet, DogsMixin):

    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Dog.objects.all()
        serializer = DogSerializer(queryset, many=True)
        print(self.get_average_age())
        return Response(serializer.data)

