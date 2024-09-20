"""Модуль URL Определяет шаблоны URL для конечных точек API."""
from django.urls import include, path
from rest_framework import routers

from .views import (
    UserViewSet,
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet)

router_v1 = routers.DefaultRouter()
router_v1.register('recipes', RecipeViewSet, basename='recipes')
router_v1.register('ingredients', IngredientViewSet, basename='ingredients')
router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
