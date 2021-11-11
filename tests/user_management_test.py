import pytest
from assertion.common_assertion import *
from clients.user_client import UserClient
from clients.data_client import DataClient

client = UserClient()
data = DataClient()
update_user_data = data.get_test_data('test_update_user_data', 2)

def test_create_new_user():
    created_playload, status_code = client.create_user()
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(created_playload, read_by="id")
    assert_status_codes_are_matched(200, status_code)
    assert_created_user_has_correct_time(read_playload, created_playload)
    assert_indificators_are_matched(read_playload, created_playload)

def test_delete_user():
    created_playload, status_code = client.create_user()
    assert_status_codes_are_matched(200, status_code)

    status_code = client.delete_user(created_playload)
    assert_status_codes_are_matched(200, status_code)
    __, status_code = client.read_user(created_playload, read_by="id")
    assert_status_codes_are_matched(500, status_code)

@pytest.mark.parametrize('current_playload, desired_playload', update_user_data)    
def test_update_user_data(current_playload, desired_playload):
    status_code = client.update_user_data(desired_playload) 
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(desired_playload, read_by="email")
    assert_status_codes_are_matched(200, status_code)
    assert_indificators_are_matched(desired_playload, read_playload)
    assert_updation_has_effects(read_playload, desired_playload)
    
    status_code = client.update_user_data(current_playload) 
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(current_playload, read_by="id")
    assert_status_codes_are_matched(200, status_code)
    assert_indificators_are_matched(current_playload, read_playload)
    assert_updation_has_effects(read_playload, current_playload)