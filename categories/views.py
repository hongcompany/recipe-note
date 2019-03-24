from rest_framework import generics

# Create your views here.
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListByOwner(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Category.objects.filter(owner=owner, is_deleted=False).order_by('-created_at')


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
