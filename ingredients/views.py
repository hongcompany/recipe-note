from rest_framework import generics

from .models import Ingredients
from .serializers import IngredientsSerializer


# Create your views here.

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class IngredientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
