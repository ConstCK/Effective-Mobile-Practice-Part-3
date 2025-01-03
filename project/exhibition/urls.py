from django.urls import path, include
from rest_framework import routers

dogs_router = routers.DefaultRouter()
breeds_router = routers.DefaultRouter()

urlpatterns = [
    path('dogs/', include(dogs_router.urls)),
    path('breeds/', include(breeds_router.urls)),
    ]