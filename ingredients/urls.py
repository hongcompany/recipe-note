from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', IngredientList.as_view()),
    path('<int:pk>/', IngredientsDetail.as_view())
]