"""URL manager tests."""

import django ;

from source.models import Urls

django.setup()
from django.test import TestCase
from rest_framework import status

from source.utils.manager import Url
# from .data import url_valid, url_not_valid, url_exist


class ManagerTestCase(TestCase):
    """Class TestUrlManager."""

    url_manager = Url()

    def test_generate_short_url(self) -> None:
        short_url = self.url_manager.generate_short_url()

        assert "http://" in short_url
        assert len(short_url) == 17

    def test_check_url_exist(self) -> None:
        assert self.url_manager.url_exist("http://1234.com") is False

    def test_create_valid_url(self) -> None:
        result = self.url_manager.create_url({"url": "http://facebook.fr"})
        assert result.status_code == status.HTTP_201_CREATED

    def test_create_not_valid_url(self) -> None:
        result = self.url_manager.create_url({"url": "http://facebook"})
        assert result.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_existing_url(self) -> None:
        # self.url_manager.create_url({"url": "http://facebook"})
        Urls.objects.create(full_path="http://facebook", short_path="http://1234567891")
        result = self.url_manager.create_url({"url": "http://facebook.fr"})
        # assert result.status_code == status.HTTP_400_BAD_REQUEST
