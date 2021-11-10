

def assert_status_codes_are_matched(actual_code, excepted_code):
    assert actual_code == excepted_code, f'{actual_code} is not mathced with {excepted_code}'
        
        
def assert_parameters_of_created_user_are_corrected(read_playload, created_playload): 
    # Extract of an account
    read_playload = read_playload["account"]
    assert read_playload["username"] == created_playload["username"], "Read username != created username"
    assert read_playload["email"] == created_playload["email"], "Read email != created email"
    assert read_playload["id"] == created_playload["id"], "Read id != created id"
    # Delay should be less than 5 sec
    assert created_playload["timestamp"] + 5 >= int(read_playload["created"]) >= created_playload["timestamp"], "Creation time is not correct"
    assert created_playload["timestamp"] + 5 >= int(read_playload["updated"]) >= created_playload["timestamp"], "Updation time is not correct"        