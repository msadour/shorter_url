"""Urls file."""

from .views import UrlViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"url", UrlViewSet, basename="url")

urlpatterns = router.urls
