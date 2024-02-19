```python
import unittest
from application import Application, submitApplication, updateApplicationStatus

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.application = Application()
        self.user_profile = {
            'user_id': '123',
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'experience': '5 years',
            'skills': ['Python', 'Django', 'JavaScript']
        }
        self.job_position = 'Developer'
        self.job_id = '456'
        self.application_form = {
            'user_id': self.user_profile['user_id'],
            'job_id': self.job_id,
            'cover_letter': 'I am passionate about coding.',
            'resume': 'path/to/resume.pdf'
        }

    def test_submitApplication(self):
        response = submitApplication(self.application_form)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'Application submitted successfully.')

    def test_updateApplicationStatus(self):
        new_status = 'reviewed'
        response = updateApplicationStatus(self.application_form['user_id'], self.job_id, new_status)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'Application status updated successfully.')
        self.assertEqual(response['data']['application_status'], new_status)

if __name__ == '__main__':
    unittest.main()
```