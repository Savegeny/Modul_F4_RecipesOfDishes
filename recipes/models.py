from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    composition = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, through='RecipeGroup')


class RecipeGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
