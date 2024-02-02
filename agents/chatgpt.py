```python
from models.programmer import Programmer
from services.hiring_service import HIRING_SERVICE
from config import settings

class ChatGPTAgent:
    def __init__(self):
        self.programmer_requirements = self.get_programmer_requirements()

    def get_programmer_requirements(self):
        return Programmer.get_requirements()

    def hire_programmer(self, candidate_info):
        programmer = Programmer(candidate_info)
        if programmer.meets_requirements(self.programmer_requirements):
            result = HIRING_SERVICE.hire_programmer(programmer)
            if result:
                return settings.PROGRAMMER_HIRE_SUCCESS
            else:
                return settings.PROGRAMMER_HIRE_FAILURE
        else:
            return settings.PROGRAMMER_HIRE_FAILURE

CHAT_AGENT = ChatGPTAgent()
```