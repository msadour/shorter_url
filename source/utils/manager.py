import string
from random import choice

import validators
from http import HTTPStatus
from rest_framework.response import Response

from source.models import Urls


class Url:
    @classmethod
    def generate_short_url(cls):
        """Generate a random and unique short url."""
        short_base_url = "".join(
            choice(string.ascii_letters + string.digits) for _ in range(10)
        )
        full_short_url = "http://" + short_base_url
        if Urls.objects.filter(short_path=full_short_url):
            return cls.generate_short_url()
        return full_short_url

    @classmethod
    def check_url_exist(cls, url):
        return not Urls.objects.filter(full_path=url).exists()

    @classmethod
    def is_url(cls, url):
        return validators.url(url)

    @classmethod
    def generate_response(cls, message, code):
        return Response(data={"message": message}, status=code)

    @classmethod
    def create_url(cls, payload):
        url = payload.data.get("url")
        short_url = cls.generate_short_url()

        if not cls.is_url(url):
            return cls.generate_response(message="Error during create url. PLease provide a good url format", code=HTTPStatus.BAD_REQUEST)

        if not cls.check_url_exist(url):
            return cls.generate_response(message="Error during create url. This url already exists.", code=HTTPStatus.BAD_REQUEST)

        Urls.objects.create(full_path=url, short_path=short_url)

        return cls.generate_response(message=f"{url} was created successfully. His short url is {short_url}", code=HTTPStatus.CREATED)
