

def assert_status_codes_are_matched(excepted_code, actual_code):
    assert actual_code == excepted_code, f'{excepted_code} is not mathced with {actual_code}'
        
def assert_indificators_are_matched(read_playload, expected_playload):
    assert read_playload["username"] == expected_playload["username"], "read_playload.username != expected_playload.username"
    assert read_playload["email"] == expected_playload["email"], "read_playload.email != expected_playload.email"
    assert read_playload["id"] == expected_playload["id"], "read_playload.id != expected_playload. id"  
          
def assert_created_user_has_correct_time(read_playload, expected_playload): 
    assert expected_playload["timestamp"] + 5 >= int(read_playload["created"]) >= expected_playload["timestamp"], "Creation time is not correct"
    assert expected_playload["timestamp"] + 5 >= int(read_playload["updated"]) >= expected_playload["timestamp"], "Updation time is not correct" 
    
def assert_updation_has_effects(read_playload, expected_playload):
    assert read_playload["created"] == expected_playload["created"], "Creation time is not correct" 
    assert read_playload["updated"] > expected_playload["updated"], "Updation is not changed"
       
           