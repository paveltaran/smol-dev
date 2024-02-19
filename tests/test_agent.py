```python
import unittest
from unittest.mock import patch, MagicMock
from agent import Agent

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()

    @patch('agent.Agent.submitApplication')
    def test_submitApplication(self, mock_submitApplication):
        mock_submitApplication.return_value = True
        result = self.agent.submitApplication()
        self.assertTrue(result)

    @patch('agent.Agent.updateApplicationStatus')
    def test_updateApplicationStatus(self, mock_updateApplicationStatus):
        mock_updateApplicationStatus.return_value = "Application Status Updated"
        result = self.agent.updateApplicationStatus()
        self.assertEqual(result, "Application Status Updated")

    @patch('agent.Agent.offerJob')
    def test_offerJob(self, mock_offerJob):
        mock_offerJob.return_value = "Job Offered"
        result = self.agent.offerJob()
        self.assertEqual(result, "Job Offered")

    @patch('agent.Agent.startRecruitmentProcess')
    def test_startRecruitmentProcess(self, mock_startRecruitmentProcess):
        mock_startRecruitmentProcess.return_value = "Recruitment Process Started"
        result = self.agent.startRecruitmentProcess()
        self.assertEqual(result, "Recruitment Process Started")

    @patch('agent.Agent.contactRecruiter')
    def test_contactRecruiter(self, mock_contactRecruiter):
        mock_contactRecruiter.return_value = "Recruiter Contacted"
        result = self.agent.contactRecruiter()
        self.assertEqual(result, "Recruiter Contacted")

if __name__ == '__main__':
    unittest.main()
```