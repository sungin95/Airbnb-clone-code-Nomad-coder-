from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    # ForeignKey와 비슷하지만 유니크한 속성을 가진다.
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Video File"
