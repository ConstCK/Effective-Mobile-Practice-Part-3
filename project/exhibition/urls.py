from django.urls import path, include
from rest_framework import routers

from .views import DogViewSet, BreedViewSet

dogs_router = routers.DefaultRouter()
breeds_router = routers.DefaultRouter()
dogs_router.register('dogs', DogViewSet)
dogs_router.register('breeds', BreedViewSet)

urlpatterns = [
    path('', include(dogs_router.urls)),
    path('', include(breeds_router.urls)),
]
