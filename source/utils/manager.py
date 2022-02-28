"""Urls manager file."""

import string
from random import choice

import validators
from http import HTTPStatus
from rest_framework.response import Response

from source.models import Urls


class Url:
    """Class Url."""

    @classmethod
    def generate_short_url(cls) -> str:
        """Generate a random and unique short url.

        Returns:
            short url.
        """
        short_base_url = "".join(
            choice(string.ascii_letters + string.digits) for _ in range(10)
        )
        full_short_url = "http://" + short_base_url
        if Urls.objects.filter(short_path=full_short_url):
            return cls.generate_short_url()
        return full_short_url

    @classmethod
    def url_exist(cls, url) -> bool:
        """Check if url already exist on db.

        Args:
            url:

        Returns:
            Url exists or not.
        """
        return Urls.objects.filter(full_path=url).exists()

    @classmethod
    def is_url(cls, url: str) -> bool:
        """Generate a random and unique short url.

        Args:
            url:

        Returns:
            url is well formatted or not.
        """
        return validators.url(url)

    @classmethod
    def generate_response(cls, message: str, code: int) -> Response:
        """Generate response.

        Args:
            message:
            code:

        Returns:
            Response with message and status code.
        """
        return Response(data={"message": message}, status=code)

    @classmethod
    def create_url(cls, payload: dict) -> Response:
        """Create url in db.

        Args:
            payload:

        Returns:
            Response with url created.
        """
        url = payload.get("url")
        short_url = cls.generate_short_url()

        if not cls.is_url(url):
            return cls.generate_response(
                message="Error during create url. PLease provide a good url format",
                code=HTTPStatus.BAD_REQUEST,
            )

        if cls.url_exist(url):
            return cls.generate_response(
                message="Error during create url. This url already exists.",
                code=HTTPStatus.BAD_REQUEST,
            )

        Urls.objects.create(full_path=url, short_path=short_url)

        return cls.generate_response(
            message=f"{url} was created successfully. His short url is {short_url}",
            code=HTTPStatus.CREATED,
        )
