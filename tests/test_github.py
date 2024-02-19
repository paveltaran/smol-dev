```python
import unittest
from github import GitHub

class TestGitHub(unittest.TestCase):

    def setUp(self):
        self.github = GitHub()

    def test_offerJob(self):
        job_position = "Developer"
        salary = 180000
        benefits = ["Health insurance coverage", "Retirement savings plan", "Flexible work schedule", "Generous vacation and paid time off", "Professional development opportunities"]
        self.github.offerJob(job_position, salary, benefits)
        self.assertEqual(self.github.job_position, job_position)
        self.assertEqual(self.github.salary, salary)
        self.assertEqual(self.github.benefits, benefits)

    def test_startRecruitmentProcess(self):
        self.github.startRecruitmentProcess()
        self.assertTrue(self.github.recruitment_started)

    def test_contactRecruiter(self):
        recruiter_contact = "recruiter@github.com"
        self.github.contactRecruiter(recruiter_contact)
        self.assertEqual(self.github.recruiter_contact, recruiter_contact)

if __name__ == '__main__':
    unittest.main()
```