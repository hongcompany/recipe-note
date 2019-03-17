from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('ingredients/', IngredientList.as_view()),
    path('ingredients/<int:pk>/', IngredientsDetail.as_view())
]