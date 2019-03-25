from rest_framework import generics

from .serializers import *


# Create your views here.

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers


