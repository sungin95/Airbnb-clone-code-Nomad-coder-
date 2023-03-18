from rest_framework.test import APITestCase
from .models import Amenity
from users.models import User


class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity Des"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        # self.client는 get/post/put/delete가 된다.
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )

    # def test_two_plus_two(self):
    #     self.assertEqual(2 + 2, 5, "The math is wrong.")
    # client는 API client를 말하는건데, API 서버로 request를 보낼 수 있게 해 준다.
    # self.client.login()

    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."
        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        # print(data)
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )

        response = self.client.post(self.URL)

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test DESC"

    def setUp(self):
        Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2/")

        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1/")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    # code challenge
    def test_put_amenity(self):
        URL = "/api/v1/rooms/amenities/1/"
        put_amenity_name = "Put Amenity"
        put_amenity_description = "Put Amenity desc."

        response = self.client.put(
            URL,
            amenity=Amenity.objects.get(pk=1),
            data={
                "name": put_amenity_name,
                "description": put_amenity_description,
            },
            partial=True,
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(
            data["name"],
            put_amenity_name,
        )

        self.assertEqual(
            data["description"],
            put_amenity_description,
        )

    # code challenge
    def test_not_put_amenity(self):
        URL = "/api/v1/rooms/amenities/1/"
        put_amenity_name = "Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity Put Amenity "
        put_amenity_description = "Put Amenity desc."

        response = self.client.put(
            URL,
            amenity=Amenity.objects.get(pk=1),
            data={
                "name": put_amenity_name,
                "description": put_amenity_description,
            },
            partial=True,
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1/")
        self.assertEqual(response.status_code, 204)


class TestRooms(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")

        self.assertEqual(response.status_code, 403)
        # 그냥 로그인 시켜 버리기~
        self.client.force_login(
            self.user,
        )
