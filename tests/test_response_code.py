import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}

payload_login = {
    "email": "peter@klaven"
}


def test_user_not_found():
    response = requests.get('https://reqres.in/api/unknown/23')
    assert response.status_code == 404


def test_create_user_201():
    response = requests.post('https://reqres.in/api/users', data=payload)
    assert response.status_code == 201


def test_get_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200


def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')
    assert response.status_code == 204


def test_login():
    response = requests.post('https://reqres.in/api/login', data=payload_login)
    assert response.status_code == 400
