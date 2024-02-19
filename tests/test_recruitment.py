```python
import unittest
from recruitment import RecruitmentProcess

class TestRecruitmentProcess(unittest.TestCase):

    def setUp(self):
        self.recruitment = RecruitmentProcess()

    def test_startRecruitmentProcess(self):
        self.recruitment.startRecruitmentProcess()
        self.assertTrue(self.recruitment.recruitment_started)

    def test_offerJob(self):
        self.recruitment.offerJob("Developer", 180000, ["Health insurance", "Retirement savings plan", "Flexible work schedule", "Generous vacation and paid time off", "Professional development opportunities"])
        self.assertEqual(self.recruitment.job_position, "Developer")
        self.assertEqual(self.recruitment.salary, 180000)
        self.assertEqual(self.recruitment.benefits, ["Health insurance", "Retirement savings plan", "Flexible work schedule", "Generous vacation and paid time off", "Professional development opportunities"])

    def test_contactRecruiter(self):
        self.recruitment.contactRecruiter("lmyabc")
        self.assertEqual(self.recruitment.recruiter_contact, "lmyabc")

if __name__ == '__main__':
    unittest.main()
```