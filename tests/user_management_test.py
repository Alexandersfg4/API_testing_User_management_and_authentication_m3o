import pytest
from assertion.common_assertion import *
from clients.user_client import UserClient
from clients.data_client import DataClient

client = UserClient()
data = DataClient()

#DONE
def test_create_new_user():
    created_playload, status_code = client.create_user()
    assert_status_codes_are_matched(200, status_code)
    data.write_playload(created_playload, 'test_update_new_user')
    read_playload, status_code = client.read_user(created_playload, read_by="id")
    assert_status_codes_are_matched(200, status_code)
    assert_parameters_of_created_user_are_corrected(read_playload, created_playload)

#DONE
def test_delete_user():
    created_playload, status_code = client.create_user()
    assert_status_codes_are_matched(200, status_code)
    read_playload, status_code = client.read_user(created_playload, read_by="id")
    assert_status_codes_are_matched(200, status_code)
    assert_parameters_of_created_user_are_corrected(read_playload, created_playload)
    print(created_playload["id"])
    status_code = client.delete_user(read_playload)
    assert_status_codes_are_matched(200, status_code)
    __, status_code = client.read_user(created_playload, read_by="username")
    assert_status_codes_are_matched(500, status_code)
    
def test_update_user_data():
    created_playload = data.get_playloads('test_update_user_data')[1]
    updated_playload = data.get_playloads('test_update_user_data')[0]
    playload, status_code = client.update_user_data(created_playload, updated_playload) 
    assert_status_codes_are_matched(200, status_code)
    read_playload, status_code = client.read_user(created_playload, read_by="id")
    assert_status_codes_are_matched(200, status_code)
    assert_that_updation_has_effects(updated_playload, read_playload)
    