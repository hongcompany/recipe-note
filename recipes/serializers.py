from rest_framework import serializers

from .models import *
from tools.serializers import ToolsSerializer
from categories.serializers import CategorySerializer
from ingredients.serializers import IngredientsSerializer


class RecipeToolsSerializers(serializers.ModelSerializer):
    tool = ToolsSerializer(many=False, read_only=True)

    class Meta:
        model = RecipeTools
        fields = ['tool']


class RecipeIngredientsSerializers(serializers.ModelSerializer):
    ingredient = IngredientsSerializer(many=False, read_only=True)

    class Meta:
        model = RecipeDetailsIngredients
        fields = ['ingredient', 'amount']


class RecipeDetailsSerializers(serializers.ModelSerializer):
    recipe_details_ingredients = RecipeIngredientsSerializers(many=True, read_only=True)

    class Meta:
        model = RecipeDetails
        fields = '__all__'


class RecipeSerializers(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=False)
    recipe_tools = RecipeToolsSerializers(many=True, read_only=False)
    recipe_details = RecipeDetailsSerializers(many=True, read_only=False)

    class Meta:
        model = Recipe
        fields = '__all__'
