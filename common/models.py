from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 데이터 베이스에 보여 주지마! 다른 모델 설계를 위한 용도야!!! abstract
    class Meta:
        abstract = True
