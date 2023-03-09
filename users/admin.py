from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # editable=False로 처리 된것을 여기서도 처리해야 admin에서 문제가 안생긴다.
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username", "password", "name", "email", "is_host"),
                # "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )
    # fieldsets = None
    # fields = ("email", "password", "name")
    list_display = ("username", "email", "name", "is_host")
