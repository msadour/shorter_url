"""Datas fixture file."""

import pytest


@pytest.fixture
def url_valid() -> str:
    return "http://google.fr"


@pytest.fixture
def url_not_valid() -> str:
    return "http://google"


@pytest.fixture
def url_exist() -> str:
    return "http://youtube.fr"
