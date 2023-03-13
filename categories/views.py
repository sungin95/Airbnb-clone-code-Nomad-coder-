from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
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
            new_category = serializer.save()  # 자동으로 create메서드를 찾는다

            return Response(
                CategorrySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


"""
{
"name": "Category from DRF",
"kind": "rooms"
}
"""


# GET /categories/1
@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = CategorrySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorrySerializer(
            category,
            data=request.data,
            partial=True,  # 부분 수정할 거란걸 말해줘야 한다.
        )
        if serializer.is_valid():
            updated_category = (
                serializer.save()
            )  # category, data=request.data 두개를 주어서 update를 호출할 거란걸 안다.
            return Response(CategorrySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)


{
    "kind": "lalalala",
}
