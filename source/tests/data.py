"""Datas fixture file."""

import pytest


@pytest.fixture(scope='class')
def url_valid() -> dict:
    return {"url": "http://facebook.fr"}


@pytest.fixture(scope='class')
def url_not_valid() -> dict:
    return {"url": "http://facebook"}


@pytest.fixture(scope='class')
def url_exist() -> dict:
    return {"url": "http://facebook.fr"}
