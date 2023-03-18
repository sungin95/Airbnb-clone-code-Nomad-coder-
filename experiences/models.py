from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start_at = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self) -> str:
        return self.name

    def total_perks(self):
        return self.perks.count()

    def rating(experience):
        count = experience.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in experience.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    explanation = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
