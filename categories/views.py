from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializes import CategorrySerializer

# GET /categories


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorrySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorrySerializer(data=request.data)
        if serializer.is_valid():
            return Response({"created": True})
        else:
            return Response(serializer.errors)


# {
# "name": "Category from DRF",
# "kind": "rooms"
# }


# GET /categories/1
@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorrySerializer(category)

    return Response(serializer.data)
