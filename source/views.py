""""Views module."""

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from source.models import Urls
from source.utils.manager import Url
from source.utils.serializers import UrlsSerializer


class UrlViewSet(viewsets.ViewSet):
    """Urls viewset."""

    url = Url()
    serializer_class = UrlsSerializer

    def list(self, request: Request) -> Response:
        """Retrieve url(s).

        Args:
          request:

        Returns:
          Response with urls.
        """
        queryset = Urls.objects.all().order_by("-created_at")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request: Request) -> Response:
        """Create a shorter url.

        Args:
          request:

        Returns:
          Response with url created.
        """
        return self.url.create_url(payload=request.data)
