import requests
import pytest
import config

def test_login_user(create_new_user):
    # create user
    created_data = create_new_user
    # log in by user
    response = requests.post(
        url=f"{config.BASE_URL_USER}Login",
        headers=config.HEADERS,
        json={
            "email": created_data['email'],
            "password": created_data['password']
            }
        )
    login_data = response.json()["session"]    
    assert response.status_code == 200, "Status code should be equal 200"    
    # read session 
    data = {
    "sessionId": login_data['id']
    }
    response = requests.post(
        url=f"{config.BASE_URL_USER}ReadSession",
        headers=config.HEADERS,
        json=data
        )
    session_data = response.json()["session"]
    assert response.status_code == 200
    assert created_data['id'] == session_data["userId"]