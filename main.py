```python
from agents.chatgpt import CHAT_AGENT
from models.programmer import PROGRAMMER
from services.hiring_service import HIRING_SERVICE
from utils.database import DATABASE
from config import settings

def init_chat_agent():
    CHAT_AGENT.initialize()

def hire_programmer():
    programmer_requirements = CHAT_AGENT.get_programmer_requirements()
    programmer = PROGRAMMER(programmer_requirements)
    hiring_result = HIRING_SERVICE.hire_programmer(programmer)
    if hiring_result:
        DATABASE.save_programmer(programmer)
        print(settings.PROGRAMMER_HIRE_SUCCESS)
    else:
        print(settings.PROGRAMMER_HIRE_FAILURE)

if __name__ == "__main__":
    init_chat_agent()
    hire_programmer()
```