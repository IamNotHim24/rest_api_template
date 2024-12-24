from django.urls import path
from .views import getUsers,createUser,userDetails

urlpatterns = [
    path('users/',getUsers,name='getUsers'),
    path("users/create/", createUser, name="create"),
    path('users/<int:pk>',userDetails,name='userDetail')
]
