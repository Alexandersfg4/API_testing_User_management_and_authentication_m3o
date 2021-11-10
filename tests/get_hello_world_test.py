import requests
import config

# DONE 
def test_get_hello_world_positive():
    response = requests.get(url=config.BASE_URL_HELLO, headers=config.HEADERS)
    assert response.status_code == 200, "Status code should be equal 200"
    assert response.json()['message'] == 'Hello ', "Value of the message should be equal 'Hello '"   

def test_get_hello_world_not_auth():
    response = requests.get(url=config.BASE_URL_HELLO)
    assert response.status_code == 401, "Status code should be equal 401"      