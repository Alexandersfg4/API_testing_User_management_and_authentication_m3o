# import pytest
# import requests
# import config
# import time

# @pytest.fixture
# def create_new_user():
#     unix_timestamp = int(time.time())
#     # Create unique user
#     data = {
#     "email": f"user{unix_timestamp}@test.com",
#     "id": f"usrid-{unix_timestamp}",
#     "password": "mySecretPass123",
#     "username": f"usrname-{unix_timestamp}"
#     }
#     response = requests.post(
#         url=f"{config.BASE_URL_USER}Create",
#         headers=config.HEADERS,
#         json=data
#         )
#     assert response.status_code == 200
#     # Write unix timestamp to dict 
#     data['timestamp'] = unix_timestamp
#     return data  