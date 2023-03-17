# 목표는 request.user 먼저 인증 후 views로 간다.

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
import jwt
from django.conf import settings


class TrustMeBroAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("Trust-Me")
        if not username:
            # 시도 x
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # 이게 규칙
        except User.DoesNotExist:
            # 시도 하지만 잘못된 정보.
            raise AuthenticationFailed(f"No user {username}")

        # # user를 찾아야 하니까 headers를 확인해 보자
        # print(request.headers)


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Jwt")
        if not token:
            return None
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )
        pk = decoded.get("pk")
        if not pk:
            raise AuthenticationFailed("Invalid Token")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed("User Not Found")
