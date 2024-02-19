```python
from datetime import datetime, timedelta
from github import GitHubAPI
from application import ApplicationForm
from database import Database

class Recruitment:
    def __init__(self, github_api_key, database_connection_string):
        self.github = GitHubAPI(github_api_key)
        self.db = Database(database_connection_string)
        self.job_position = "Developer"
        self.salary = 180000
        self.benefits = ["Health insurance coverage", "Retirement savings plan", "Flexible work schedule", "Generous vacation and paid time off", "Professional development opportunities"]
        self.application_deadline = datetime.now() + timedelta(hours=24)
        self.recruiter_contact = "GitHub Recruitment Team"

    def start_recruitment_process(self, user_id):
        user_profile = self.github.get_user_profile(user_id)
        if not user_profile:
            return "User not found"
        
        application_form = ApplicationForm(user_profile)
        application_status = "Pending"
        self.db.save_application_to_database(user_id, application_form, application_status)
        
        return "Application started. Please fill out the form at https://auth.githubtalentcommunity.online/"

    def submit_application(self, user_id, application_form):
        if datetime.now() > self.application_deadline:
            return "Application deadline has passed"
        
        self.db.save_application_to_database(user_id, application_form, "Submitted")
        return "Application submitted. We will review your application and contact you soon."

    def update_application_status(self, user_id, status):
        self.db.update_application_status(user_id, status)
        return f"Application status updated to {status}"

    def offer_job(self, user_id):
        user_profile = self.github.get_user_profile(user_id)
        if not user_profile:
            return "User not found"
        
        job_offer = {
            "job_position": self.job_position,
            "salary": self.salary,
            "benefits": self.benefits,
            "recruiter_contact": self.recruiter_contact
        }
        
        self.github.send_message(user_id, "JobOffer", job_offer)
        return "Job offer sent"
```