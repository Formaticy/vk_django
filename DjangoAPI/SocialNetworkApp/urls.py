from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<str:username>/', views.UsersDetail.as_view()),

    path('statuses/', views.StatusesList.as_view()),
    path('statuses/<int:pk>/', views.StatusesDetail.as_view()),

    path('friends/', views.FriendsList.as_view()),
    path('friends/delete/', views.FriendsDelete.as_view()),
    path('friends/detail/outcoming_proposals/<int:friend_one_id>/', views.FriendsOutcomingProposals.as_view()),
    path('friends/detail/incoming_proposals/<int:friend_one_id>/', views.FriendsIncomingProposals.as_view()),
    path('friends/detail/already_friends/<int:friend_one_id>/', views.FriendsAlreadyFriends.as_view()),
    path('friends/detail/reject_proposal/', views.FriendsReject.as_view()),
    path('friends/detail/accept_proposal/', views.FriendsAccept.as_view()),
    re_path(r'^friends/detail/status/(?P<friend_one_id>(\d+))/(?P<friend_two_id>(\d+))/$', views.FriendsStatus.as_view()),
]