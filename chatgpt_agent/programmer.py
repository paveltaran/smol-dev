```python
from chatgpt_agent.database import Database
from chatgpt_agent.utils import validate_programmer_data

class Programmer:
    def __init__(self, database: Database):
        self.database = database

    def create_programmer(self, programmer_data: dict):
        if validate_programmer_data(programmer_data):
            return self.database.insert('programmers', programmer_data)
        else:
            raise ValueError("Invalid programmer data")

    def update_programmer(self, programmer_id: int, updated_data: dict):
        if validate_programmer_data(updated_data):
            return self.database.update('programmers', programmer_id, updated_data)
        else:
            raise ValueError("Invalid updated data")

    def delete_programmer(self, programmer_id: int):
        return self.database.delete('programmers', programmer_id)

    def get_programmer(self, programmer_id: int):
        return self.database.select('programmers', programmer_id)
```