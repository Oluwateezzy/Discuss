from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.Discuss_login, name="login"),
    path("register/", views.discuss_register, name="register"),
    path("logout/", views.Discuss_logout, name="logout"),
    path("room/<str:pk>", views.room, name="room"),
    path("profile/<str:pk>", views.user_profile, name="profile"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>/", views.deleteMessage, name="delete-message"),
]
