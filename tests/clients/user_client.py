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
        try:
            id = playload["id"]
        except KeyError:
            print(f"It's not a created playload, is it read playload?") 
            try:
                id = playload["account"]["id"]
            except KeyError:
                    print(f"It's not a read playload too!") 
                    raise ("id not found in the palyload") 
        playload = {
            "id": id  
        }                
        response = self.request.delete(f"{self.base_url}Delete", playload, self.headers)
        return response.status_code