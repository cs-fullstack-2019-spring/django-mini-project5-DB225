from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newProfile/', views.newProfile, name="newProfile"),
    path('profile/', views.profile, name="profile"),
    path('editProfile/<int:id>/', views.editProfile, name="editProfile"),
    path('deleteProfile/<int:id>/', views.deleteProfile, name="deleteProfile"),
    path('newRecipe/', views.newRecipe, name="newRecipe"),
    path('allRecipe/', views.allRecipe, name="allRecipe"),
    path('editRecipe/<int:id>/', views.editRecipe, name="edit"),
    path('deleteRecipe/<int:id>/', views.deleteRecipe, name="delete"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
