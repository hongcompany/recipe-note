from django.shortcuts import render
from rest_framework import generics

from .serializers import *


# Create your views here.

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers


class RecipeListByOwner(generics.ListAPIView):
    serializer_class = RecipeSerializers

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Recipe.objects.filter(owner=owner, is_deleted=False).order_by('-created_at')


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = RecipeSerializers


def index(request):
    name = "" # 여기 바꿔서 보여주시오.
    return render(request, 'recipes/index.html', { 'name': name })
