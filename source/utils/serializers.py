"""Serializers module."""

from rest_framework import serializers

from source.models import Urls


class UrlsSerializer(serializers.ModelSerializer):
    """Class UrlsSerializer."""

    full_path = serializers.CharField(required=False)
    short_path = serializers.CharField(required=False)

    class Meta:
        """Class Meta."""

        model = Urls
        fields = [
            "full_path",
            "short_path",
        ]
