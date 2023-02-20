from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "address",
        ("price_per_night", "pets_allowed"),
    )
    list_display = ["name", "price_per_night", "address", "pets_allowed"]
    list_filter = ["price_per_night", "pets_allowed"]
    search_fields = ["address"]  # _startswith  텍스트로 시작하는 것만 검색
    # search_fields 는 반드시 리스트 혹은 튜플이어야 한다. string이면 안된다.
    list_display_links = ("name", "address")
    list_editable = ("pets_allowed",)
