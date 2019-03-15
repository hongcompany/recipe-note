from .models import Tools
from rest_framework import serializers


class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'
