from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    # 클릭시 파라미터가 설정값으로 뜬다.
    parameter_name = "word"

    def lookups(self, request, model_admin):
        # 2번째 인자가 보임
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    # 새로 고침하면 아래가 실행
    # 주의 사항 항상 실행되니까 None인 상황을 대비해 준다.
    def queryset(self, request, reviews):
        # print(self.value())  # 무엇을 클릭했는지 알 수 있다.
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return


class good_bad_reviews(admin.SimpleListFilter):
    title = "reviews good or bad"

    parameter_name = "check"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        check = self.value()
        if check == "good":
            return reviews.filter(rating__gte=3)
        elif check == "bad":
            return reviews.filter(rating__lt=3)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        good_bad_reviews,
        "rating",
        "user__is_host",  # review에서 user의 정보로 필터를 만들 수 있다.
        "room__category",
        "room__pet_friendly",
    )
