from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    # 세션, 쿠키
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    # 토큰
    # username과 password보내면 token반환
    path("token-login", obtain_auth_token),
    # JWT 토큰
    path("jwt-login", views.JWTLogIn.as_view()),
    # 소설로그인
    path("github", views.GithubLogin.as_view()),
    # @는 인스타에서도 사용하니까 그냥 붙이는거.
    path("@<str:username>", views.PublicUser.as_view()),
    path("@<str:username>/rooms", views.UserRooms.as_view()),
    path("@<str:username>/reviews", views.UserReviews.as_view()),
]
