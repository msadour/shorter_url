""""Views module."""

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from source.utils.manager import Url


class MailViewSet(viewsets.ViewSet):
    """
    Mail viewset.
    """

    url = Url()

    def list(self, request: Request) -> Response:
        """Retrieve url(s).

        Args:
          request:

        Returns:
          Response with urls.
        """
        pass

    def create(self, request: Request) -> Response:
        """Create a shorter url.

        Args:
          request:

        Returns:
          Response with url created.
        """
        pass
