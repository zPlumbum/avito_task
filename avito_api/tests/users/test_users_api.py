import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


@pytest.mark.django_db
def test_users_create(api_client):
    url = reverse('user-list')
    user_payload = {
        "username": "user6",
        "first_name": "Kiril",
        "last_name": "Krit",
        "user_balance": 300
    }

    response = api_client.post(url, user_payload, format='json')

    assert response.status_code == HTTP_201_CREATED
    response_json = response.json()
    assert response_json['first_name'] == user_payload['first_name']
    assert float(response_json['user_balance']) == user_payload['user_balance']


@pytest.mark.django_db
def test_users_get(api_client, user_factory):
    user = user_factory()

    url = reverse('user-detail', args=[user.id])

    response = api_client.get(url)

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert response_json['id'] == user.id


@pytest.mark.django_db
def test_users_list(api_client, user_factory):
    user1 = user_factory()
    user2 = user_factory()

    url = reverse('user-list')

    response = api_client.get(url)

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json) == 2
    result_ids = {user['id'] for user in response_json}
    assert {user1.id, user2.id} == result_ids


@pytest.mark.django_db
def test_change_user_balance(api_client, user_factory):
    user = user_factory()

    url = reverse('user_balance')
    user_payload = {
        "user_id": user.id,
        "value": 100
    }

    response = api_client.post(url, user_payload, format='json')

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_to_user_transaction(api_client, user_factory):
    user1 = user_factory(user_balance=200)
    user2 = user_factory()

    url = reverse('transaction')
    user_payload = {
        "from_user_id": user1.id,
        "to_user_id": user2.id,
        "value": 100
    }

    response = api_client.post(url, user_payload, format='json')

    assert response.status_code == HTTP_200_OK
