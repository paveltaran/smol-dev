```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from programmer import Programmer
from config import DATABASE_URI

Base = declarative_base()

class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)

    def connect_to_db(self):
        return self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def add_programmer(self, programmer):
        session = self.connect_to_db()
        session.add(programmer)
        session.commit()

    def get_programmer(self, id):
        session = self.connect_to_db()
        return session.query(Programmer).filter_by(id=id).first()

    def update_programmer(self, id, update):
        session = self.connect_to_db()
        programmer = session.query(Programmer).filter_by(id=id).first()
        for key, value in update.items():
            setattr(programmer, key, value)
        session.commit()

    def delete_programmer(self, id):
        session = self.connect_to_db()
        programmer = session.query(Programmer).filter_by(id=id).first()
        session.delete(programmer)
        session.commit()
```