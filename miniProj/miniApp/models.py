from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserLoginModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    profilePicture = models.CharField(max_length=800)
    password = models.CharField(max_length=200, default="")
    userForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class RecipesModel(models.Model):
    picture = models.CharField(max_length=800)
    name = models.CharField(max_length=100)
    description = models.TextField()
    dateCreate = models.DateField(default="2019-01-01")
    creator = models.CharField(max_length=100)
    ingredients = models.TextField()
    directions_for_meal = models.TextField()
    recipeForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name