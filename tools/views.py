from rest_framework import generics

from .models import Tools
from .serializers import ToolsSerializer


# Create your views here.

class ToolList(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer


class ToolsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
