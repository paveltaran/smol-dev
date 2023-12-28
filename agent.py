```python
import requests
from programmer import Programmer

class Agent:
    def __init__(self, token):
        self.token = token

    def hire_request(self, programmer_id):
        programmer = self.get_programmer(programmer_id)
        if programmer:
            return self.hire_programmer(programmer)
        else:
            return "Programmer not found."

    def get_programmer(self, programmer_id):
        response = requests.get(f"https://api.github.com/users/{programmer_id}")
        if response.status_code == 200:
            data = response.json()
            return Programmer(data['id'], data['login'], data['email'])
        else:
            return None

    def hire_programmer(self, programmer):
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'programmer_id': programmer.id, 'programmer_name': programmer.name}
        response = requests.post("https://api.hireprogrammer.com/hire", headers=headers, data=data)
        if response.status_code == 200:
            return "Programmer hired successfully."
        else:
            return "Failed to hire programmer."
```