from django.views.generic import ListView
from .models import Recipe, Group


# Create your views here.
class RecipesList(ListView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipes'


