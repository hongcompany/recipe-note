from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('recipes/', RecipeList.as_view()),
    path('recipes/<slug:owner>/', RecipeListByOwner.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),
]