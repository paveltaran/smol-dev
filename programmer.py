```python
from sqlalchemy import Column, Integer, String
from database import Base

class Programmer(Base):
    __tablename__ = 'programmers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    expertise = Column(String(120), unique=False)
    availability = Column(String(120), unique=False)

    def __init__(self, name=None, expertise=None, availability=None):
        self.name = name
        self.expertise = expertise
        self.availability = availability

    def __repr__(self):
        return '<Programmer %r>' % (self.name)
```