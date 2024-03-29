# System logic of fetching data and inserting into DB.

# Inside services.py
from sqlalchemy.orm import sessionmaker
from .models import engine, Activity  # Import the engine and models from models.py

Session = sessionmaker(bind=engine)

def insert_activity(data):
    session = Session()
    new_activity = Activity(**data)  # Assuming data is a dict that matches the Activity model
    session.add(new_activity)
    session.commit()
    session.close()
