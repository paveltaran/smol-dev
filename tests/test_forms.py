```python
import unittest
from forms import ApplicationForm

class TestForms(unittest.TestCase):

    def setUp(self):
        self.form = ApplicationForm()

    def test_fillForm(self):
        self.form.fillForm(user_id="123", job_id="456", user_profile={"name": "John Doe", "experience": 5})
        self.assertEqual(self.form.user_id, "123")
        self.assertEqual(self.form.job_id, "456")
        self.assertEqual(self.form.user_profile, {"name": "John Doe", "experience": 5})

    def test_validateForm(self):
        self.form.fillForm(user_id="123", job_id="456", user_profile={"name": "John Doe", "experience": 5})
        self.assertTrue(self.form.validateForm())

    def test_submitApplication(self):
        self.form.fillForm(user_id="123", job_id="456", user_profile={"name": "John Doe", "experience": 5})
        self.assertTrue(self.form.submitApplication())

if __name__ == '__main__':
    unittest.main()
```