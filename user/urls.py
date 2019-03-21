from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view())
]