from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
)


router = DefaultRouter()
router.register('crud', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
