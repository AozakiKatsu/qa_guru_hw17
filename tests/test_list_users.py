import requests
from jsonschema import validate
from schemas.schemas import list_users


def test_get_user():
    response = requests.get('https://reqres.in/api/users?page=2')
    assert response.status_code == 200
    body = response.json()
    print(response.text)
    validate(body, list_users)
