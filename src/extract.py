from config import garmin_email, garmin_password
from garminconnect import (
  Garmin,
  GarminConnectAuthenticationError,
  GarminConnectConnectionError,
  GarminConnectTooManyRequestsError
)

import logging
from datetime import datetime, timedelta
import requests
from getpass import getpass
from garth.exc import GarthHTTPError

from models import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


email = garmin_email
password = garmin_password
api = None
tokenstore = ".garminconnect"

def init_api(email, password):
  try:
    print(
      f"Trying to login to Garmin Connect using token data from '{tokenstore}'...\n"
    )
    garmin = Garmin()
    garmin.login(tokenstore)
  except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError):
    # print(
    #   "Login tokens not present, login with your Garmin Connect credentials to generate them.\n"
    #   f"They will be stored in '{tokenstore}' for future use.\n"
    # )
    try:
      garmin = Garmin(email, password)
      garmin.login()
      # Save tokens for next login
      garmin.garth.dump(tokenstore)
    except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError, requests.exceptions.HTTPError) as err:
      logger.error(err)
      return None
  return garmin


if not api:
  api = init_api(email, password)




# testing API calls
start_date = (datetime.today() - timedelta(days=2)).date()
end_date = datetime.today().date()

info = api.get_full_name()
# info2 = api.get_blood_pressure(start_date)
# info2 = api.get_daily_weigh_ins(start_date)
# info2 = api.get_weigh_ins(start_date, end_date)
# info3 = api.get_user_profile()
# info3 = api.get_stress_data(start_date)
# info3 = api.get_heart_rates(start_date)
info3 = api.get_sleep_data(start_date)


# Inserting into DB
def insert_steps(data):  # Keep the function name as is
    session = Session()
    try:
        for entry in data:
            row = Step_tbl(  # Assuming StepsData is your model
                start_gmt=datetime.strptime(entry["startGMT"], "%Y-%m-%dT%H:%M:%S.%f"),
                end_gmt=datetime.strptime(entry["endGMT"], "%Y-%m-%dT%H:%M:%S.%f"),
                steps=entry["steps"],
                pushes=entry["pushes"],
                primaryActivityLevel=entry["primaryActivityLevel"],
                activity_level=entry["activityLevelConstant"]
            )
            session.add(row)
        
        session.commit()
        print("Step data successfully inserted into the database.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
        print("Session closed")
        
        


if __name__ == "__main__":
  
  current_date = start_date
  
  while current_date <= end_date: 
    
    steps_data = api.get_steps_data(current_date)
    insert_steps(steps_data)
    
    # stress_data = api.get_stress_data(current_date) = shit
    # insert_stress(stress_data)
    
    # heart_rate = api.get_heart_rates(current_date)
    
    # body_battery = api.get_body_battery(current_date)
    
    # floors = api.get_floors(current_date)
    
    # rhr_day = api.get_rhr_day(current_date)
    
    # sleep_data = api.get_sleep_data(current_date)
    
    # 
    
    # respiration_data = api.get_respiration_data(current_date)
    
    # spo2_data = api.get_spo2_data(current_date)
    # max_metrics = api.get_max_metrics(current_date)
    
    current_date += timedelta(days=1)
    print(current_date)
    print(f"Completed: {current_date}") 