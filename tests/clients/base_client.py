from decouple import config

class BaseClient:
    def __init__(self):
        self.headers = {
    "Authorization": f"Bearer {config('API_KEY')}",
    "Content-Type": "application/json"
    }
        
   