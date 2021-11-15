import pytest
from assertion.common_assertion import *
from clients.user_client import UserClient
from clients.data_client import DataClient

client = UserClient()
data = DataClient()
user_data = data.get_test_data('test_user_can_be_updated', 4)
not_existed_user = data.get_test_data('test_user_can_not_be_updated', 1)[0]

@pytest.mark.parametrize('current_playload, read_by_d, desired_playload, read_by_c', user_data)    
def test_user_can_be_updated(current_playload, read_by_d, desired_playload, read_by_c):
    status_code = client.update_user_data(desired_playload) 
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(desired_playload, read_by=read_by_d)
    assert_status_codes_are_matched(200, status_code)
    assert_user_data_as_expected(desired_playload, read_playload)
    assert_updation_time_is_changed(read_playload, desired_playload)
    
    status_code = client.update_user_data(current_playload) 
    assert_status_codes_are_matched(200, status_code)
    
    read_playload, status_code = client.read_user(current_playload, read_by=read_by_c)
    assert_status_codes_are_matched(200, status_code)
    assert_user_data_as_expected(current_playload, read_playload)
    assert_updation_time_is_changed(read_playload, current_playload)
    
def test_user_can_not_be_updated():
    status_code = client.update_user_data(not_existed_user) 
    assert_status_codes_are_matched(500, status_code)
   