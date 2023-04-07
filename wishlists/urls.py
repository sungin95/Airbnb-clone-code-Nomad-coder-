from django.urls import path
from .views import Wishlists, WishlstDetail, WishlistToggle

urlpatterns = [
    path("", Wishlists.as_view()),
    path("<int:pk>", WishlstDetail.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", WishlistToggle.as_view()),
]
