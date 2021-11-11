import time

from clients.base_client import BaseClient
from clients.config import BASE_URL_USER
from clients.request import APIRequest


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.base_url = BASE_URL_USER
        self.request = APIRequest()
        
    def create_user(self, body=None):
       playload = self.__create_unique_user(body)
       return playload
       
    def __create_unique_user(self, body=None):
        unix_timestamp = int(time.time())
        if body is None:
            playload = {
            "email": f"user{unix_timestamp}@test.com",
            "id": f"usrid-{unix_timestamp}",
            "password": "mySecretPass123",
            "username": f"usrname-{unix_timestamp}"
            } 
        else:
            playload = body
        
        response = self.request.post(f"{self.base_url}Create", playload, self.headers)
        playload["timestamp"] = unix_timestamp
        return playload, response.status_code 
    
    def read_user(self, created_playload, read_by="id"):
        playload = self.__create_playload_for_reading(created_playload, read_by)
        response = self.request.post(f"{self.base_url}Read", playload, self.headers)
        return response.as_dict, response.status_code
        
        
    def __create_playload_for_reading(self, created_playload, read_by="id"):
        try:
            playload = {
                read_by: created_playload[read_by]
                }
        except KeyError:
            print(f"{read_by} is incorrect key, returned empty dict") 
            return {}     
        return playload 
    
    def delete_user(self, playload):
        id = self.__get_value_from_playload(playload)
        playload = {
            "id": id  
        }                
        response = self.request.delete(f"{self.base_url}Delete", playload, self.headers)
        return response.status_code
    
    def __get_value_from_playload(self, playload, value="id"):
        try:
            value = playload[value]
        except KeyError:
            print(f"It's not a created playload, is it read playload?") 
            try:
                value = playload["account"][value]
            except KeyError:
                    print(f"It's not a read playload too!") 
                    raise ("id not found in the palyload") 
        return value        
        
    def update_user_data(self, now_playload, future_playload):
        playload = {
            'id': self.__get_value_from_playload(now_playload)
        }
        now_username = self.__get_value_from_playload(now_playload, "username")
        future_username = self.__get_value_from_playload(future_playload, "username")
        now_email = self.__get_value_from_playload(now_playload, "email")
        future_email = self.__get_value_from_playload(future_playload, "email")
        print(f"{now_email} and {future_email}")
        if now_username != future_username:
            playload['username'] = future_username
        if now_email != future_email:
            playload['email'] = future_email   
        response = self.request.put(f"{self.base_url}Update", playload, self.headers)
        return playload, response.status_code   
        