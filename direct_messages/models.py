from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):

    """Room Model Definition"""

    participants = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self):
        return f"{self.user} sats: {self.text}"
