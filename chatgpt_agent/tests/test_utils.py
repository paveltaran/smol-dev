import unittest
from chatgpt_agent import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "name": "John Doe",
            "skills": ["Python", "Java", "C++"],
            "experience": 5
        }

    def test_validate_programmer_data(self):
        result = utils.validate_programmer_data(self.sample_data)
        self.assertTrue(result)

    def test_format_programmer_data(self):
        result = utils.format_programmer_data(self.sample_data)
        expected_result = "Name: John Doe, Skills: Python, Java, C++, Experience: 5 years"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()