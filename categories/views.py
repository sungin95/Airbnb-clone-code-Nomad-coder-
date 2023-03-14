from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Category
from .serializes import CategorrySerializer


class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorrySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorrySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()  # 자동으로 create메서드를 찾는다

            return Response(
                CategorrySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


class CategoryDetaiil(APIView):
    # 이건 관습이다.
    # 디테일한 부분을 가져 올떄는 이 방식으로 한다.
    # category를 사용 할거면 아래를 이용한다.
    # self.get_object(pk)
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = CategorrySerializer(self.get_object(pk))
        # print(serializer)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorrySerializer(
            self.get_object(pk),
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

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
