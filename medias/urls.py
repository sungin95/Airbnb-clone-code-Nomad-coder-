from django.urls import path
from .views import PhotoDetail, GetUploadURL

urlpatterns = [
    # 따라만 쳐 놓음
    path("photos/get-url", GetUploadURL.as_view()),
    #
    path("photos/<int:pk>", PhotoDetail.as_view()),
]
