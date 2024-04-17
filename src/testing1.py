from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Engine, engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import db_host, db_username, db_password, db_name, db_schema, db_port
import pyodbc
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base = declarative_base()

class Hrate_day_tbl(Base):
    __tablename__ = 'etl_hrate_day'
    __table_args__ = {'schema': f"{db_schema}"}
    userProfilePK = Column(Integer, primary_key=True)
    calendarDate = Column(DateTime)
    startTimestampGMT = Column(DateTime)
    endTimestampGMT = Column(DateTime)
    maxHeartRate = Column(Integer)
    minHeartRate = Column(Integer)
    restingHeartRate = Column(Integer)
    lastSevenDaysAvgRestingHeartRate = Column(Integer)

class Steps_tbl(Base):
    __tablename__ = 'etl_steps'
    __table_args__ = {'schema': f"{db_schema}"}
    startGMT = Column(DateTime, primary_key=True)
    endGMT = Column(DateTime)
    steps = Column(Integer)
    primaryActivityLevel = Column(String)
    activityLevelConstant = Column(Boolean)

# Construct the database URL for MS Azure SQL
# DATABASE_URL = f"mssql+pyodbc://{db_username}:{db_password}@{db_host}:1433/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"

def get_engine_db(bulk: bool=True) -> Engine:
    con_str = engine.URL.create(
        "mssql+pyodbc",
        username=db_username,
        password=db_password,
        host=db_host,
        database=db_name,
        port=db_port,
        query={
            "driver": 'ODBC Driver 17 for SQL Server',
            "LongAsMax": "Yes",
        }
    )
    return create_engine(con_str, fast_executemany=bulk, echo=True)

engine = get_engine_db()

Session = sessionmaker(bind=engine)

def setup_db():
    try:
        Base.metadata.create_all(engine)
        logger.info("Database setup completed successfully.")
    except Exception as e:
        logger.error("Database setup failed:", exc_info=True)

if __name__ == "__main__":
    logger.info("Starting database setup.")
    # print(DATABASE_URL)
    setup_db()