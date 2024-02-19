```python
import unittest
from programmer import Programmer

class TestProgrammer(unittest.TestCase):

    def setUp(self):
        self.programmer = Programmer()

    def test_updateUserProfile(self):
        user_profile = {
            'user_id': '123',
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'skills': ['Python', 'JavaScript', 'C++']
        }
        self.programmer.updateUserProfile(user_profile)
        self.assertEqual(self.programmer.user_profile, user_profile)

    def test_retrieveUserProfile(self):
        user_profile = {
            'user_id': '123',
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'skills': ['Python', 'JavaScript', 'C++']
        }
        self.programmer.user_profile = user_profile
        retrieved_profile = self.programmer.retrieveUserProfile()
        self.assertEqual(retrieved_profile, user_profile)

if __name__ == '__main__':
    unittest.main()
```