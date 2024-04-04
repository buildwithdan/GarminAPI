# SQLAlchemy database models

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date, JSON, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
# Import your configuration settings
from config import db_host, db_username, db_password, db_name, db_port, db_schema

Base = declarative_base()

# class BodyBattery_tbl(Base):
#     __tablename__ = 'etl_body_battery'
#     __table_args__ = {'schema': f"{db_schema}"}
#     date = Column(Date)
#     charged = Column(Integer)
#     drained = Column(Integer)
#     start_timestamp_gmt = Column(DateTime, primary_key=True)
#     end_timestamp_gmt = Column(DateTime)
#     body_battery_values = Column(JSON)  # Storing the array directly; consider normalization

# class Floor_tbl(Base):
#     __tablename__ = 'etl_floor'
#     __table_args__ = {'schema': f"{db_schema}"}
#     start_gmt = Column(DateTime, primary_key=True)
#     end_gmt = Column(DateTime)
#     floors_ascended = Column(Integer)
#     floors_descended = Column(Integer)

class Hrate_day_tbl(Base):
    __tablename__ = 'etl_hrate_day'
    __table_args__ = {'schema': f"{db_schema}"}
    userProfilePK = Column(Integer, primary_key=True)
    calendarDate = Column(DateTime)
    startTimestampGMT = Column(DateTime)
    endTimestampGMT = Column(DateTime)
    startTimestampLocal = Column(DateTime)
    endTimestampLocal = Column(DateTime)
    maxHeartRate = Column(Integer)
    minHeartRate = Column(Integer)
    restingHeartRate = Column(Integer)
    lastSevenDaysAvgRestingHeartRate = Column(Integer)






class Hrate_min_tbl(Base):
    __tablename__ = 'etl_hrate_min'
    __table_args__ = {'schema': f"{db_schema}"}
    timestamp = Column(DateTime, primary_key=True)
    heartrate = Column(Integer)
    
# class MaxMetrics_tbl(Base):
#     __tablename__ = 'etl_maxmetrics'
#     __table_args__ = {'schema': f"{db_schema}"}
#     calendar_date = Column(DateTime, primary_key=True)
#     vo2_max_precise_value = Column(Float)
#     fitness_age = Column(Integer)
#     heat_acclimation_percentage = Column(Float)
#     # Add more fields as needed from maxmetrics.json
 
# class Respiration_tbl(Base):
#     __tablename__ = 'etl_respiration'
#     __table_args__ = {'schema': f"{db_schema}"}
#     start_timestamp_gmt = Column(DateTime, primary_key=True)
#     end_timestamp_gmt = Column(DateTime)
#     # Include specific fields for respiration data 

# class RestingHeart_tbl(Base):
#     __tablename__ = 'etl_resting_heart'
#     __table_args__ = {'schema': f"{db_schema}"}
#     user_profile_id = Column(Integer)
#     statistics_start_date = Column(Date, primary_key=True)
#     statistics_end_date = Column(Date)
#     value = Column(Float)
#     calendar_date = Column(Date)

# class Sleep_tbl(Base):
#     __tablename__ = 'etl_sleep'
#     __table_args__ = {'schema': f"{db_schema}"}
#     start_gmt = Column(DateTime, primary_key=True)
#     end_gmt = Column(DateTime)
#     sleep_level = Column(String)
#     # Add more fields as per your sleep.json structure

# class SpO2_tbl(Base):
#     __tablename__ = 'etl_spo2'
#     __table_args__ = {'schema': f"{db_schema}"}
#     start_timestamp_gmt = Column(DateTime, primary_key=True)
#     end_timestamp_gmt = Column(DateTime)
#     average_spo2 = Column(Float)
#     lowest_spo2 = Column(Integer)
#     spo2_hourly_averages = Column(JSON)  # Storing JSON directly, consider normalization

class Steps_tbl(Base):
    __tablename__ = 'etl_steps'
    __table_args__ = {'schema': f"{db_schema}"}
    startGMT = Column(DateTime, primary_key=True)
    endGMT = Column(DateTime)
    steps = Column(Integer)
    pushes = Column(Integer)
    primaryActivityLevel = Column(String)
    activityLevelConstant = Column(Boolean)

# class Stress_tbl(Base):
#     __tablename__ = 'etl_stress'
#     __table_args__ = {'schema': f"{db_schema}"}
#     user_profile_pk = Column(Integer)
#     calendar_date = Column(Date)
#     start_timestamp_gmt = Column(DateTime, primary_key=True)
#     end_timestamp_gmt = Column(DateTime)
#     max_stress_level = Column(Integer)
#     avg_stress_level = Column(Integer)
#     stress_values = Column(JSON)  # Storing the array directly; consider normalization


# class personal_records_tbl(Base):
#     __tablename__ = 'etl_personal_records'
#     id = Column(Integer, primary_key=True)
#     typeId = Column(Integer)
#     activityId = Column(Integer)
#     activityName = Column(String)
#     activityType = Column(String)
#     activityStartDateTimeInGMT = Column(DateTime)
#     actStartDateTimeInGMTFormatted = Column(String)
#     activityStartDateTimeLocal = Column(DateTime)
#     activityStartDateTimeLocalFormatted = Column(String)
#     value = Column(Float)
#     prStartTimeGmt = Column(Integer)
#     prStartTimeGmtFormatted = Column(String)
#     prStartTimeLocal = Column(Integer)
#     prStartTimeLocalFormatted = Column(String)
#     prTypeLabelKey = Column(String)
#     poolLengthUnit = Column(String)


# Construct the database URL for Azure SQL
# MS Azure SQL
DATABASE_URL = f"mssql+pyodbc://{db_username}:{db_password}@{db_host}:1433/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"

# Postgres
# DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL, echo=True, fast_executemany=True)
Session = sessionmaker(bind=engine)

def create_all_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_all_tables()


# Read up about the fast_exceutemany... on what is it trying to CAST?