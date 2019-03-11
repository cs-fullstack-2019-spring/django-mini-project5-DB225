from django.contrib import admin
from .models import UserLoginModel, RecipesModel

# Register your models here.
admin.site.register(UserLoginModel)
admin.site.register(RecipesModel)
