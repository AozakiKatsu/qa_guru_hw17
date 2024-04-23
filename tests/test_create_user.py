import requests
from jsonschema import validate
from schemas.schemas import create

payload = {
    "name": "morpheus",
    "job": "leader"
}


def test_get_user():
    response = requests.post('https://reqres.in/api/users', data=payload)
    assert response.status_code == 201
    body = response.json()
    print(response.text)
    validate(body, create)
    assert body["name"] == 'morpheus'
    assert body["job"] == "leader"
