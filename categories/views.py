from django.shortcuts import render
from .models import Category
from django.http import JsonResponse


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok": True,
            "categories": all_categories,  # 동작 안한다. 이걸 serializable을 통해 바꾸어 보내주어야 한다.
        }
    )
