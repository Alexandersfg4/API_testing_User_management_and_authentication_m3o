

def assert_status_codes_are_matched(excepted_code, actual_code):
    assert actual_code == excepted_code, f'{excepted_code} is not mathced with {actual_code}'
        
        
def assert_parameters_of_created_user_are_corrected(read_playload, created_playload): 
    # Extract of an account
    read_playload = read_playload["account"]
    assert read_playload["username"] == created_playload["username"], "Read username != created username"
    assert read_playload["email"] == created_playload["email"], "Read email != created email"
    assert read_playload["id"] == created_playload["id"], "Read id != created id"
    # Delay should be less than 5 sec
    assert created_playload["timestamp"] + 5 >= int(read_playload["created"]) >= created_playload["timestamp"], "Creation time is not correct"
    assert created_playload["timestamp"] + 5 >= int(read_playload["updated"]) >= created_playload["timestamp"], "Updation time is not correct" 
    
def assert_that_updation_has_effects(updated_playload, read_playload):
    read_playload = read_playload["account"]
    assert read_playload["username"] == updated_playload["username"], "Read username != created username"
    assert read_playload["email"] == updated_playload["email"], "Read email != created email"
    assert read_playload["created"] == updated_playload["created"], "Creation time is not correct" 
    assert read_playload["updated"] > updated_playload["updated"], "Updation is not changed" 
           