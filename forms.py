```python
from datetime import datetime
from marshmallow import Schema, fields, validate

class ApplicationFormSchema(Schema):
    user_id = fields.Str(required=True)
    job_id = fields.Str(required=True)
    application_date = fields.DateTime(missing=datetime.utcnow)
    user_profile = fields.Dict(required=True)
    application_status = fields.Str(validate=validate.OneOf(["Submitted", "Under Review", "Accepted", "Rejected"]), missing="Submitted")

def fillForm(user_id, job_id, user_profile):
    form = ApplicationFormSchema()
    application_form = {
        "user_id": user_id,
        "job_id": job_id,
        "user_profile": user_profile
    }
    return form.load(application_form)

def validateForm(application_form):
    form = ApplicationFormSchema()
    errors = form.validate(application_form)
    if errors:
        raise ValueError(errors)
    return True
```