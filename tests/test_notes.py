from fastapi.testclient import TestClient
import time

def test_create_note(client: TestClient):
    response = client.post(
        '/notes',
        json={
            'text': 'Записка 1',
            'ttl_seconds': 30
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data['key']
    assert data['ttl_seconds'] == 30

def test_get_created_note(client: TestClient):
    first_response = client.post(
        '/notes',
        json={
            'text': 'Записка 2',
            'ttl_seconds': 30
        }
    )

    assert first_response.status_code == 201

    data = first_response.json()

    assert data['key']
    assert data['ttl_seconds'] == 30

    key = data['key']

    second_response = client.get(
        f'/notes/{key}'
    )

    assert second_response.status_code == 200

    second_data = second_response.json()

    assert key == second_data['key']
    assert second_data['text'] == 'Записка 2'


def test_get_404_note(client):
    key = 'asd'
    response = client.get(
        f'/notes/{key}'
    )

    assert response.status_code == 404

def test_delete_note(client):
    first_response = client.post(
        '/notes',
        json={
            'text': 'Записка 2',
            'ttl_seconds': 30
        }
    )

    assert first_response.status_code == 201

    data = first_response.json()

    assert data['key']
    assert data['ttl_seconds'] == 30

    key = data['key']

    second_response = client.delete(
        f'/notes/{key}'
    )

    assert second_response.status_code == 204

    third_response = client.delete(
        f'/notes/{key}'
    )

    assert third_response.status_code == 404



def test_delete_404_note(client):
    key = '123'
    response = client.delete(
        f'/notes/{key}'
    )

    assert response.status_code == 404


def test_null_ttl(client):
    response = client.post(
        '/notes',
        json={
            'text': 'Записка 1',
            'ttl_seconds': 0
        }
    )

    assert response.status_code == 422


def test_minus_ttl(client):
    response = client.post(
        '/notes',
        json={
            'text': 'Записка 1',
            'ttl_seconds': -5
        }
    )

    assert response.status_code == 422

def test_something_is_none(client):
    response = client.post(
        '/notes',
        json={
            'text': 'Записка 1'
        }
    )

    assert response.status_code == 422


def test_time_exited(client):
    response = client.post(
        '/notes',
        json={
            'text': 'Заметка 1',
            'ttl_seconds': 1
        }
    )

    assert response.status_code == 201

    data = response.json()
    key = data['key']

    time.sleep(1)

    second_response = client.get(
        f'/notes/{key}'
    )

    assert second_response.status_code == 404


def test_create_two_notes(client):
    first_response = client.post(
        '/notes',
        json={
            'text': 'Заметка 1',
            'ttl_seconds': 30
        }
    )

    assert first_response.status_code == 201

    data = first_response.json()

    first_key = data['key']

    second_response = client.post(
        '/notes',
        json={
            'text': 'Заметка 2',
            'ttl_seconds': 30
        }
    )

    assert second_response.status_code == 201
    second_data = second_response.json()
    second_key = second_data['key']
    assert first_key != second_key

    third_response = client.get(
        f'/notes/{first_key}'
    )

    third_data = third_response.json()
    first_text = third_data['text']

    fourth_response = client.get(
        f'/notes/{second_key}'
    )

    fourth_data = fourth_response.json()
    second_text = fourth_data['text']

    assert first_text != second_text