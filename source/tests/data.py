"""Datas fixture file."""

import pytest


@pytest.fixture(scope='class')
def url_valid() -> dict:
    """Fixture with valid url.

    Returns:
        payload.
    """
    return {"url": "http://facebook.fr"}


@pytest.fixture(scope='class')
def url_not_valid() -> dict:
    """Fixture with not valid url.

    Returns:
        payload.
    """
    return {"url": "http://facebook"}


@pytest.fixture(scope='class')
def url_exist() -> dict:
    """Fixture with existing url.

    Returns:
        payload.
    """
    return {"url": "http://facebook.fr"}
