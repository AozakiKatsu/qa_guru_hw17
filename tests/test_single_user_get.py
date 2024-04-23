import requests
from jsonschema import validate
from schemas.schemas import single_user


def test_get_user():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200
    body = response.json()
    print(response.text)
    validate(body, single_user)
    assert body["data"]["id"] == 2
    assert body["data"]["email"] == "janet.weaver@reqres.in"


def test_get_user_negative():
    response = requests.get('https://reqres.in/api/users/200')
    assert response.json() == {}
