import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_factory():

    def factory(**kwargs):
        return baker.make('user_balance.User', **kwargs)

    return factory
