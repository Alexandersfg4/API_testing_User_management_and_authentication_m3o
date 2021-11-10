import requests
import pytest
import config


def test_create_new_user(create_new_user):
    # create user
    created_data = create_new_user
    # read created user by id
    response = requests.post(
        url=f"{config.BASE_URL_USER}Read",
        headers=config.HEADERS,
        json={
            "id": created_data['id']
            }
        )
    read_data = response.json()["account"]
    assert response.status_code == 200, "Status code should be eaqual 200"
    assert read_data["username"] == created_data["username"], "Requested username == created username"
    assert read_data["email"] == created_data["email"], "Requested email == created email"
    # Delay should be less than 5 sec
    assert created_data["timestamp"] + 5 >= int(read_data["created"]) >= created_data["timestamp"], "Check creation time"
    assert created_data["timestamp"] + 5 >= int(read_data["updated"]) >= created_data["timestamp"], "Check updation time"


def test_dselete_user_1(create_new_user):
    # create user
    created_data = create_new_user
    # delete user
    response = requests.delete(
        url=f"{config.BASE_URL_USER}Delete",
        headers=config.HEADERS,
        json={
            "id": created_data['id']
        }
        )
    assert response.status_code == 200, "Status code should be eaqual 200"
    # read created user by id
    response = requests.post(
        url=f"{config.BASE_URL_USER}Read",
        headers=config.HEADERS,
        json={
            "id": created_data['id']
        }
        )
    assert response.status_code == 500, "Status code should be eaqual 500"   


