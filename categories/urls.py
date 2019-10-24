from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', CategoryList.as_view()),
    path('<int:pk>/', CategoryDetail.as_view())
]