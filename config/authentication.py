# 목표는 request.user 먼저 인증 후 views로 간다.

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


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
