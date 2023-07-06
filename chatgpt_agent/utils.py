```python
import re
from chatgpt_agent.config import EMAIL_REGEX, PHONE_REGEX

def validate_email(email):
    if re.search(EMAIL_REGEX, email):
        return True
    return False

def validate_phone(phone):
    if re.search(PHONE_REGEX, phone):
        return True
    return False

def format_programmer_data(programmer):
    formatted_data = {
        'name': programmer.name,
        'email': programmer.email,
        'phone': programmer.phone,
        'skills': ', '.join(programmer.skills),
        'experience': programmer.experience
    }
    return formatted_data
```