```python
from datetime import datetime, timedelta
from forms import ApplicationForm
from database import saveApplicationToDatabase, retrieveApplicationFromDatabase
from utils import validateForm

class Application:
    def __init__(self, user_id, job_id):
        self.user_id = user_id
        self.job_id = job_id
        self.application_status = "Not Submitted"
        self.application_form = ApplicationForm()
        self.application_deadline = datetime.now() + timedelta(hours=24)

    def submitApplication(self):
        if validateForm(self.application_form):
            saveApplicationToDatabase(self)
            self.application_status = "Submitted"
            return True
        else:
            return False

    def updateApplicationStatus(self, new_status):
        self.application_status = new_status
        saveApplicationToDatabase(self)

    def retrieveApplication(self):
        application_data = retrieveApplicationFromDatabase(self.user_id, self.job_id)
        if application_data:
            self.application_status = application_data['application_status']
            self.application_form = application_data['application_form']
            self.application_deadline = application_data['application_deadline']
```