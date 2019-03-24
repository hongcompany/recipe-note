from enum import Enum

from django.db import models
from django.utils.datetime_safe import datetime

from categories.models import Category
from tools.models import Tools


# Create your models here.

class Recipe(models.Model):
    owner = models.CharField(max_length=200)  # 추후 user로 변경됨
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now())
    is_template = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Recipe[ owner: %s, category: %s, created_at: %s]" % (self.owner, self.category.name, self.created_at)

    def recipe_summary(self):
        summary = self.recipesummary
        return "%s : %s" % (summary.title, summary.content)

    def recipe_tools(self):
        tools = RecipeTools.objects.filter(recipe=self)
        return [t.__str__() for t in tools]

    def category_info(self):
        return "%s:%s" % (self.owner, self.category.name)

    # def recipedetails(self):
    #     return self.recipedetails_set(id=self.id)


class Level(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"


class RecipeSummary(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    level = models.CharField(max_length=20, choices=[(tag.value, tag) for tag in Level])

    # 추후 이미지 정보 추가

    def __str__(self):
        return self.title


class RecipeTools(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tools, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tool.name

# class DetailType(Enum):
#     basic = "BASIC"
#     fermentation = "FERMENTATION"
#     dough = "DOUGH"
#     oven = "OVEN"
#
# class RecipeDetails(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     description = models.CharField(max_length=200)
#     timer = models.IntegerField(null=True)
#     temperature = models.FloatField(default=0.0)
#     type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in DetailType])
#
#     # 추후 이미지 정보 추가
#     def __str__(self):
#         return "Detail[description: %s, timer: %d, temperature: %f, type: %s]" % (self.description, self.timer, self.temperature, self.type)
#
#     def get_recipe_details_ingredients(self):
#         return self.recipedetailsingredients(id=self.id)
#
#
# class RecipeDetailsIngredients(models.Model):
#     recipe_detail = models.ForeignKey(RecipeDetails, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredients, on_delete=models.DO_NOTHING)
#     amount = models.CharField(max_length=20)
#
#     def __str__(self):
#         return "Ingredient[name: %s, amount: %s]" % (self.ingredient.name, self.amount)
