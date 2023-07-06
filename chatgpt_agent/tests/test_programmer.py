```python
import unittest
from chatgpt_agent.programmer import Programmer

class TestProgrammer(unittest.TestCase):

    def setUp(self):
        self.programmer = Programmer("John Doe", "Python", 5)

    def test_create_programmer(self):
        self.assertEqual(self.programmer.name, "John Doe")
        self.assertEqual(self.programmer.language, "Python")
        self.assertEqual(self.programmer.experience, 5)

    def test_update_programmer(self):
        self.programmer.update("Jane Doe", "Java", 7)
        self.assertEqual(self.programmer.name, "Jane Doe")
        self.assertEqual(self.programmer.language, "Java")
        self.assertEqual(self.programmer.experience, 7)

    def test_delete_programmer(self):
        self.programmer.delete()
        self.assertIsNone(self.programmer.name)
        self.assertIsNone(self.programmer.language)
        self.assertIsNone(self.programmer.experience)

if __name__ == '__main__':
    unittest.main()
```