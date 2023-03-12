from django.contrib import admin
from .models import Room, Amenity


# 이렇게 설정을 해 주고 어드민 창에서 액션에 원하는 쿼리셋을 넣고 실행해 주면 아래 함수가 실행이 된다.
@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, queryset):
    print(model_admin)
    print(dir(request))
    print(queryset)
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
    )
    search_fields = (
        "owner__username"
        # "name",
        # "^price",  # ^ startwith, = 같을때,
    )

    # def total_amenities(self, room):
    #     return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
