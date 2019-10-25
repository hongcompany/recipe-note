from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', CategoryListCreateView.as_view()),
    path('<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view())
]