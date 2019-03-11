from django import forms
from .models import UserLoginModel, RecipesModel


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        exclude = ['userForeignKey']
        widgets = {
            "password": forms.PasswordInput(),
        }


class RecipesForm(forms.ModelForm):
    class Meta:
        model = RecipesModel
        exclude = ['recipeForeignKey']

