```python
import unittest
from utils import submitApplication, updateApplicationStatus, fillForm, validateForm, saveApplicationToDatabase, retrieveApplicationFromDatabase, updateUserProfile, retrieveUserProfile

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.user_profile = {
            "user_id": "123",
            "name": "Test User",
            "email": "testuser@gmail.com",
            "skills": ["Python", "Django", "JavaScript"]
        }
        self.application_form = {
            "user_id": "123",
            "job_id": "456",
            "cover_letter": "I am a great fit for this role because...",
            "resume": "path/to/resume.pdf"
        }

    def test_submitApplication(self):
        response = submitApplication(self.application_form)
        self.assertEqual(response, "Application submitted successfully")

    def test_updateApplicationStatus(self):
        response = updateApplicationStatus("123", "456", "Under Review")
        self.assertEqual(response, "Application status updated successfully")

    def test_fillForm(self):
        response = fillForm(self.user_profile, self.application_form)
        self.assertEqual(response, "Form filled successfully")

    def test_validateForm(self):
        response = validateForm(self.application_form)
        self.assertEqual(response, "Form validated successfully")

    def test_saveApplicationToDatabase(self):
        response = saveApplicationToDatabase(self.application_form)
        self.assertEqual(response, "Application saved to database successfully")

    def test_retrieveApplicationFromDatabase(self):
        response = retrieveApplicationFromDatabase("123", "456")
        self.assertEqual(response, self.application_form)

    def test_updateUserProfile(self):
        response = updateUserProfile(self.user_profile)
        self.assertEqual(response, "User profile updated successfully")

    def test_retrieveUserProfile(self):
        response = retrieveUserProfile("123")
        self.assertEqual(response, self.user_profile)

if __name__ == "__main__":
    unittest.main()
```