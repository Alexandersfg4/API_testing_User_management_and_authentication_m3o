import re

def assert_status_codes_are_matched(excepted_code, actual_code):
    assert actual_code == excepted_code, f'{excepted_code} is not mathced with {actual_code}'
        
def assert_user_data_as_expected(read_playload, expected_playload):
    assert read_playload["username"] == expected_playload["username"], "read_playload.username != expected_playload.username"
    assert read_playload["email"] == expected_playload["email"], "read_playload.email != expected_playload.email"
    assert read_playload["id"] == expected_playload["id"], "read_playload.id != expected_playload. id"  
          
def assert_created_user_has_correct_time(read_playload, expected_playload): 
    assert expected_playload["timestamp"] + 5 >= int(read_playload["created"]) >= expected_playload["timestamp"], "Creation time is not correct"
    assert expected_playload["timestamp"] + 5 >= int(read_playload["updated"]) >= expected_playload["timestamp"], "Updation time is not correct" 
    
def assert_updation_time_is_changed(read_playload, expected_playload):
    assert read_playload["created"] == expected_playload["created"], "Creation time is not correct" 
    assert read_playload["updated"] > expected_playload["updated"], "Updation is not changed"
    
def assert_read_user_was_not_found(read_playload):
    print(str(read_playload))
    assert str(read_playload).endswith("None")
    
       
           