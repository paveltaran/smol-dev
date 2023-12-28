```python
import requests
import json

def send_request(url, method='GET', data=None):
    headers = {'Content-Type': 'application/json'}
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def validate_programmer_data(data):
    required_fields = ['name', 'skills', 'experience']
    if not all(field in data for field in required_fields):
        return False
    return True
```