from rest_framework.test import APITestCase


class TestAmenities(APITestCase):
    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 5, "The math is wrong.")
        # client는 API client를 말하는건데, API 서버로 request를 보낼 수 있게 해 준다.
        # self.client.login()
