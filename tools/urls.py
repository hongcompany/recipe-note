from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('tools/', ToolList.as_view()),
    path('tools/<int:pk>/', ToolsDetail.as_view())
]