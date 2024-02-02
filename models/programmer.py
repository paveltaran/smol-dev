```python
from utils import database

class Programmer:
    def __init__(self, name, skills, experience_years):
        self.name = name
        self.skills = skills
        self.experience_years = experience_years

    def save_programmer(self):
        db = database.get_database_config()
        db.insert('programmers', self.__dict__)

    @staticmethod
    def get_programmer_requirements():
        return {
            'name': 'string',
            'skills': 'list',
            'experience_years': 'int'
        }
```