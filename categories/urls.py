from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<slug:owner>', CategoryListByOwner.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view())
]