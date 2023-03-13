from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializes import CategorrySerializer


@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorrySerializer(all_categories, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        }
    )
