import requests
from jsonschema import validate
from schemas.schemas import update_user

payload = {
    "name": "morpheus",
    "job": "zion resident"
}


def test_update_user():
    response = requests.patch('https://reqres.in/api/users/2', data=payload)
    assert response.status_code == 200
    body = response.json()
    print(response.text)
    validate(body, update_user)
    assert body["name"] == 'morpheus'
    assert body["job"] == "zion resident"
