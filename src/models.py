# SQLAlchemy database models

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
# Import your configuration settings
from config import db_host, db_username, db_password, db_name, db_port, db_schema

Base = declarative_base()

class BodyBattery(Base):
    __tablename__ = 'body_battery'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    charged = Column(Integer)
    drained = Column(Integer)
    start_timestamp_gmt = Column(DateTime)
    end_timestamp_gmt = Column(DateTime)
    body_battery_values = Column(JSON)  # Storing the array directly; consider normalization

class FloorData(Base):
    __tablename__ = 'floor_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    start_gmt = Column(DateTime)
    end_gmt = Column(DateTime)
    floors_ascended = Column(Integer)
    floors_descended = Column(Integer)

class HRData(Base):
    __tablename__ = 'hr_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    start_timestamp_gmt = Column(DateTime)
    end_timestamp_gmt = Column(DateTime)
    max_heart_rate = Column(Integer)
    min_heart_rate = Column(Integer)
    resting_heart_rate = Column(Integer)
    heart_rate_values = Column(JSON)  # Storing JSON directly, consider normalization
    
class MaxMetricsData(Base):
    __tablename__ = 'maxmetrics_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    calendar_date = Column(DateTime)
    vo2_max_precise_value = Column(Float)
    fitness_age = Column(Integer)
    heat_acclimation_percentage = Column(Float)
    # Add more fields as needed from maxmetrics.json
 
class RespirationData(Base):
    __tablename__ = 'respiration_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    start_timestamp_gmt = Column(DateTime)
    end_timestamp_gmt = Column(DateTime)
    # Include specific fields for respiration data 

class RestingHeartRate(Base):
    __tablename__ = 'resting_heart_rate'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    user_profile_id = Column(Integer)
    statistics_start_date = Column(Date)
    statistics_end_date = Column(Date)
    value = Column(Float)
    calendar_date = Column(Date)

class SleepData(Base):
    __tablename__ = 'sleep_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    start_gmt = Column(DateTime)
    end_gmt = Column(DateTime)
    sleep_level = Column(String)
    # Add more fields as per your sleep.json structure

class SpO2Data(Base):
    __tablename__ = 'spo2_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    start_timestamp_gmt = Column(DateTime)
    end_timestamp_gmt = Column(DateTime)
    average_spo2 = Column(Float)
    lowest_spo2 = Column(Integer)
    spo2_hourly_averages = Column(JSON)  # Storing JSON directly, consider normalization

class StepData(Base):
    __tablename__ = 'step_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    start_gmt = Column(DateTime)
    end_gmt = Column(DateTime)
    steps = Column(Integer)
    activity_level = Column(String)

class StressData(Base):
    __tablename__ = 'stress_data'
    __table_args__ = {'schema': f"{db_schema}"}
    id = Column(Integer, primary_key=True)
    user_profile_pk = Column(Integer)
    calendar_date = Column(Date)
    start_timestamp_gmt = Column(DateTime)
    end_timestamp_gmt = Column(DateTime)
    max_stress_level = Column(Integer)
    avg_stress_level = Column(Integer)
    stress_values = Column(JSON)  # Storing the array directly; consider normalization


# Construct the database URL for Azure SQL
# MS Azure SQL
DATABASE_URL = f"mssql+pyodbc://{db_username}:{db_password}@{db_host}:1433/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"

# Postgres
# DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

def create_all_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_all_tables()
    