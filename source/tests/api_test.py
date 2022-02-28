# from rest_framework import status
# from rest_framework.test import APIClient, APITestCase
#
# from .data import url_valid, url_not_valid
# from .factories import UrlFactory
#
#
# client = APIClient()
#
# url = "/url/"  # export DJANGO_SETTINGS_MODULE=shorter_url.settings
#
#
# class UrlTestCase(APITestCase):
#     """class ArticleTestCase."""
#
#     def setUp(self) -> None:
#         """Set up attributes for tests."""
#         self.client = APIClient()
#         UrlFactory()
#
#     def test_list(self) -> None:
#         """Test list of urls.
#         Raises:
#             AssertError: Assertion failed.
#         """
#         response = self.client.get(url)
#         breakpoint()
#         self.assertEqual(len(response.data), 1)
#
#     def test_create_valid_url(self, url_valid) -> None:
#         """
#         Test creation of an article.
#         Raises:
#             AssertError: Assertion failed.
#         """
#         response = self.client.post(
#             url, data=url_valid, content_type="application/json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     # def test_create_not_valid_url(self, url_not_valid) -> None:
#     #     """
#     #     Test creation of an invalid url.
#     #
#     #     Raises:
#     #         AssertError: Assertion failed.
#     #     """
#     #     response = self.client.post(
#     #         url, data=url_not_valid, content_type="application/json"
#     #     )
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #
#     # def test_create_existing_url(self, url_exist) -> None:
#     #     """
#     #     Test creation of an invalid url.
#     #
#     #     Raises:
#     #         AssertError: Assertion failed.
#     #     """
#     #     response = self.client.post(
#     #         url, data=url_exist, content_type="application/json"
#     #     )
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
