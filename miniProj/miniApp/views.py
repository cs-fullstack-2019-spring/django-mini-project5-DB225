from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserLoginModel, RecipesModel, RecipesForm


# Create your views here.
# Function for the index page
def index(request):
    if request.user.is_authenticated:
        userLog = UserLoginModel.objects.get(username=request.user)
        allRecipes = RecipesModel.objects.filter(recipeForeignKey=userLog)
        return render(request, 'miniApp/index.html', {'allRecipes': allRecipes})
    else:
        return render(request, 'miniApp/index.html')


# Create a new account
def newProfile(request):
    newLogin = UserLoginForm(request.POST or None)
    print(request.POST)
    if request.method == 'POST' and newLogin.is_valid():
        UserLoginModel.objects.create(username=request.POST["username"], email=request.POST['email'],
                                      profilePicture=request.POST['profilePicture'],
                                      password=request.POST["password"])
        User.objects.create_user(request.POST["username"], request.POST['email'], request.POST["password"])
        print("save")
        # newLogin.save()
        return redirect('index')

    context = {
        "newLogin": newLogin
    }

    return render(request, 'miniApp/newProfile.html', context)


# Edit the profile of the users
def editProfile(request, id):
    edit_profile = get_object_or_404(UserLoginModel, pk=id)
    profileToEdit = UserLoginForm(request.POST or None, instance=edit_profile)
    if profileToEdit.is_valid():
        profileToEdit.save()
        return redirect('index')

    return render(request, 'miniApp/editProfile.html', {'edit_profile': edit_profile})


# Delete the profiles of the users
def deleteProfile(request, id):
    deleted_profile = get_object_or_404(UserLoginModel, pk=id)
    if request.method == 'POST':
        deleted_profile.delete()
        return redirect('index')
    return render(request, 'miniApp/deleteProfile.html', {'deleted_profile': deleted_profile})


# The profile of the logged in user
def profile(request):
    allProfiles = UserLoginModel.objects.all()
    return render(request, 'miniApp/profile.html', {'allProfiles': allProfiles})


# to add a new recipe
def newRecipe(request):
    newRecipe = RecipesForm(request.POST or None)
    print(request.POST)
    print(request.user)
    # print(newRecipe)
    if newRecipe.is_valid():
        print("save")
        userLog = get_object_or_404(UserLoginModel, userForeignKey=request.user)
        # userLog = UserLoginModel.objects.get(userForeignKey=request.user)
        print(userLog)
        new_recipe = RecipesModel.objects.create(picture=request.POST["picture"], name=request.POST["name"],
                                                 description=request.POST["description"],
                                                 dateCreate=request.POST["dateCreate"], creator=request.POST["creator"],
                                                 ingredients=request.POST["ingredients"],
                                                 directions_for_meal=request.POST["directions_for_meal"],
                                                 recipeForeignKey=userLog)

        return redirect('index')
    else:
        print(newRecipe.errors)
    return render(request, 'miniApp/newRecipe.html', {"newRecipe": newRecipe})


# To print all the recipes
def allRecipe(request):
    everyRecipe = RecipesModel.objects.all()
    return render(request, 'miniApp/allRecipes.html', {'everyRecipe': everyRecipe})


# Edit the recipe
def editRecipe(request, id):
    edit_recipe = get_object_or_404(RecipesModel, pk=id)
    recipeToEdit = RecipesForm(request.POST or None, instance=edit_recipe)
    if recipeToEdit.is_valid():
        recipeToEdit.save()
        return redirect('index')

    return render(request, 'miniApp/editRecipe.html', {'newRecipe': recipeToEdit})


# Delete the recipe
def deleteRecipe(request, id):
    deleted_recipe = get_object_or_404(RecipesModel, pk=id)
    if request.method == 'POST':
        deleted_recipe.delete()
        return redirect('index')
    return render(request, 'miniApp/deleteRecipe.html', {"deleted_recipe": deleted_recipe})
