import pytest
from assertion.common_assertion import *
from clients.user_client import UserClient
from clients.data_client import DataClient

client = UserClient()
data = DataClient()
can_be_deleted = data.get_test_data('test_new_user_can_be_deleted', 1)
not_existed_user = data.get_test_data('test_not_existed_user_can_not_be_deleted', 1)

@pytest.mark.smoke_check
@pytest.mark.parametrize("read_by", can_be_deleted)    
def test_new_user_can_be_deleted(read_by):
    created_playload, status_code = client.create_user()
    assert_status_codes_are_matched(200, status_code)
    
    status_code = client.delete_user(created_playload)
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(created_playload, read_by)
    assert_status_codes_are_matched(200, status_code)
    assert_read_user_was_not_found(read_playload)

@pytest.mark.parametrize("user_data", not_existed_user)    
def test_not_existed_user_can_not_be_deleted(user_data):
    status_code = client.delete_user(user_data)
    assert_status_codes_are_matched(400, status_code)