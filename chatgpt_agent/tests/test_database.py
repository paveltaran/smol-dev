```python
import unittest
from chatgpt_agent.database import Database
from chatgpt_agent.programmer import Programmer

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.programmer = Programmer('John Doe', 'Python', 5, 'john.doe@example.com')

    def test_insert_programmer(self):
        result = self.db.insert_programmer(self.programmer)
        self.assertEqual(result, True)

    def test_select_programmer(self):
        self.db.insert_programmer(self.programmer)
        result = self.db.select_programmer(self.programmer.email)
        self.assertEqual(result.name, self.programmer.name)

    def test_update_programmer(self):
        self.db.insert_programmer(self.programmer)
        self.programmer.name = 'Jane Doe'
        result = self.db.update_programmer(self.programmer)
        self.assertEqual(result, True)

    def test_delete_programmer(self):
        self.db.insert_programmer(self.programmer)
        result = self.db.delete_programmer(self.programmer.email)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```