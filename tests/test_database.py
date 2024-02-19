```python
import unittest
from database import Database
from programmer import Programmer

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.programmer = Programmer(user_id="123", job_id="456", job_position="Developer", salary=180000, benefits=["Health insurance", "Retirement savings plan", "Flexible work schedule", "Generous vacation and paid time off", "Professional development opportunities"], application_deadline="24 hours")

    def test_saveApplicationToDatabase(self):
        result = self.db.saveApplicationToDatabase(self.programmer)
        self.assertEqual(result, True)

    def test_retrieveApplicationFromDatabase(self):
        self.db.saveApplicationToDatabase(self.programmer)
        result = self.db.retrieveApplicationFromDatabase(self.programmer.user_id)
        self.assertEqual(result, self.programmer)

if __name__ == '__main__':
    unittest.main()
```