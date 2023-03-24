from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound
from .models import Perk
from .serializer import PerkSerializer
from django.conf import settings
from django.utils import timezone  # settings의 값을 확인한다.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from django.db import transaction
from categories.models import Category
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from bookings.models import Booking
from bookings.serializers import (
    PublicBookingSerializer,
    CreateExperienceBookingSerializer,
)

from .models import Experience, Perk
from .serializer import ExperienceDetailSerializer, ExperienceListSerializer


class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)


class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk, data=request.data, partial=True)
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(PerkSerializer(updated_perk).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Experiences(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_Experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(
            all_Experiences,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceDetailSerializer(data=request.data)
        if serializer.is_valid():
            # category
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is require.")
            try:
                category = Category.objects.get(pk=category_pk)
                # experience만 선택해야 하니까
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("The category kind should be 'rooms'")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            # 트랜잭션이 작동안하면 유저에게 알려주기 위해 try
            try:
                # 트랜잭션!!! 변경사항을 기억하고 있다가 문제없이 끝나면 푸쉬
                # try,except를 사용하면 에러난 사실을 감지 못하니까 사용X
                with transaction.atomic():
                    experience = serializer.save(
                        host=request.user,
                        category=category,
                    )
                    # perks
                    perks = request.data.get("perks")
                    for perk_pk in perks:
                        perk = Perk.objects.get(pk=perk_pk)
                        experience.perks.add(perk)
                    serializer = ExperienceDetailSerializer(
                        experience, context={"request": request}
                    )
                    return Response(serializer.data)
            except Exception:
                print(serializer)
                raise ParseError("perk not found")
        else:
            return Response(serializer.errors)


class ExperienceDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        # 검증
        if experience.host != request.user:
            raise PermissionDenied

        serializer = ExperienceDetailSerializer(
            experience, data=request.data, partial=True
        )
        if serializer.is_valid():
            # category
            category_pk = request.data.get("category", experience.category.pk)
            if not category_pk:
                raise ParseError("Category is require.")
            try:
                category = Category.objects.get(pk=category_pk)
                # experiences만 선택해야 하니까
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("The category kind should be 'experiences'")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            #
            # 트랜잭션이 작동안하면 유저에게 알려주기 위해 try
            try:
                # 트랜잭션!!! 변경사항을 기억하고 있다가 문제없이 끝나면 푸쉬
                # try,except를 사용하면 에러난 사실을 감지 못하니까 사용X
                with transaction.atomic():
                    experience = serializer.save(
                        owner=request.user,
                        category=category,
                    )
                    # perks
                    perks = request.data.get("perks")
                    # none이면 pass, != 이면 clear 개로운 값 추가
                    if perks != None:
                        experience.perks.clear()
                        for perk_pk in perks:
                            perk = Perk.objects.get(pk=perk_pk)
                            experience.perks.add(perk)
                    serializer = ExperienceDetailSerializer(
                        experience, context={"request": request}
                    )
                    return Response(serializer.data)

            except Exception:
                raise ParseError("Amenity not found")
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied
        experience.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ExperienceReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = page * page_size
        experience = self.get_object(pk)
        serializer = ReviewSerializer(
            experience.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                experience=self.get_object(pk=pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            raise Response(serializer.errors)


class ExperiencePerks(APIView):
    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 3
        start = (page - 1) * page_size
        end = page * page_size
        experience = self.get_object(pk)
        serializer = PerkSerializer(
            experience.perks.all()[start:end],
            many=True,
        )
        return Response(serializer.data)


class ExperiencePhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        experience = self.get_object(pk)
        if request.user != experience.host:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(experience=experience)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class ExperienceBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk=pk)
        now = timezone.localtime(timezone.now()).date()

        bookings = Booking.objects.filter(
            experience=experience,
            kind=Booking.BookingKindChoices.EXPERIENCE,
            check_in__gt=now,
        )
        serializer = PublicBookingSerializer(
            bookings,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        experience = self.get_object(pk)
        serializer = CreateExperienceBookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(
                experience=experience,
                user=request.user,
                kind=Booking.BookingKindChoices.EXPERIENCE,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
