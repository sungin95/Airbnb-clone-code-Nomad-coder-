from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    # URLField? 처음 보네
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.URLField()
    # ForeignKey와 비슷하지만 유니크한 속성을 가진다.
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",  # 이게 맞나?
    )

    def __str__(self):
        return "Video File"
