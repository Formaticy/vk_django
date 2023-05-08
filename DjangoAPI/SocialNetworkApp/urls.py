from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<str:username>/', views.UsersDetail.as_view())
]