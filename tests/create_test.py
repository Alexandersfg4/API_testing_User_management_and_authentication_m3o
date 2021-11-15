import pytest
from assertion.common_assertion import *
from clients.user_client import UserClient
from clients.data_client import DataClient

client = UserClient()
data = DataClient()
invalid_data = data.get_test_data('test_add_user_invalid_data', 4)

@pytest.mark.smoke_check
def test_new_user_can_be_added():
    created_playload, status_code = client.create_user()
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(created_playload, read_by="id")
    assert_status_codes_are_matched(200, status_code)
    assert_created_user_has_correct_time(read_playload, created_playload)
    assert_user_data_as_expected(read_playload, created_playload)

@pytest.mark.parametrize("user_data, create_code, read_code, read_by", invalid_data)    
def test_add_user_invalid_data(user_data, create_code, read_code, read_by):
    created_playload, status_code = client.create_user(user_data)
    assert_status_codes_are_matched(create_code, status_code)
    
    read_playload, status_code = client.read_user(created_playload, read_by=read_by)
    assert_status_codes_are_matched(read_code, status_code)