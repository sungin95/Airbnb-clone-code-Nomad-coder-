from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    # @는 인스타에서도 사용하니까 그냥 붙이는거.
    path("@<str:username>", views.PublicUser.as_view()),
]
