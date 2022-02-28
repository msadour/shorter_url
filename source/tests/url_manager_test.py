# from rest_framework import status
#
# from source.utils.manager import Url
# from .data import url_valid, url_not_valid, url_exist
#
#
# class UrlManagerTestCase:
#     def setup(self) -> None:
#         self.url_manager = Url()
#
#     def test_generate_short_url(self):
#         short_url = self.url_manager.generate_short_url()
#
#         assert "http://" in short_url
#         assert len(short_url) == 17
#
#     def test_check_url_exist(self):
#         assert self.url_manager.check_url_exist("http://1234.com") is True
#
#     def test_create_valid_url(self, url_valid) -> None:
#         result = self.url_manager.create_url(url_valid)
#         assert result.status_code == status.HTTP_201_CREATED
#
#     def test_create_not_valid_url(self, url_not_valid) -> None:
#         result = self.url_manager.create_url(url_not_valid)
#         assert result.status_code == status.HTTP_400_BAD_REQUEST
#
#     def test_create_existing_url(self, url_exist) -> None:
#         result = self.url_manager.create_url(url_exist)
#         assert result.status_code == status.HTTP_400_BAD_REQUEST
