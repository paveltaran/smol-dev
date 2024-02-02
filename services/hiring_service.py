```python
from models.programmer import Programmer
from utils.database import save_programmer

def hire_programmer(programmer_requirements):
    programmer = Programmer(programmer_requirements)
    save_status = save_programmer(programmer)
    
    if save_status:
        return "PROGRAMMER_HIRE_SUCCESS"
    else:
        return "PROGRAMMER_HIRE_FAILURE"
```