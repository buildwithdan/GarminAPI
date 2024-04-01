import datetime
import logging
import os
from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError
)
from dotenv import load_dotenv

# Initialize logging and environment variables
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()

class GarminService:
    def __init__(self):
        self.email = os.getenv('GARMIN_EMAIL')
        self.password = os.getenv('GARMIN_PASSWORD')
        self.client = None

    def login(self):
        """Log into Garmin Connect to initialize the session."""
        try:
            self.client = Garmin(self.email, self.password)
            self.client.login()
        except (GarminConnectConnectionError, GarminConnectTooManyRequestsError, GarminConnectAuthenticationError) as e:
            logger.error(f"Failed to log into Garmin Connect: {e}")
            raise

    def fetch_activities(self, start_date, end_date):
        """Fetch activities within a date range."""
        if not self.client:
            self.login()
        try:
            activities = self.client.get_activities_by_date(start_date, end_date)
            return activities
        except Exception as e:
            logger.error(f"Failed to fetch activities: {e}")
            return []

    def fetch_health_data(self, start_date, end_date):
        """Fetch health data within a date range, returning a dictionary of data types."""
        if not self.client:
            self.login()
        health_data = {}
        current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            try:
                # Extend this dictionary with more data types as needed
                health_data[date_str] = {
                    'steps': self.client.get_steps_data(date_str),
                    'heart_rate': self.client.get_heart_rates(date_str),
                    'body_battery': self.client.get_body_battery(date_str),
                    # Add more API calls for different health data here
                }
            except Exception as e:
                logger.error(f"Failed to fetch health data for {date_str}: {e}")
            current_date += datetime.timedelta(days=1)
        
        return health_data

# Example usage
if __name__ == "__main__":
    service = GarminService()
    activities = service.fetch_activities("YYYY-MM-DD", "YYYY-MM-DD")
    health_data = service.fetch_health_data("YYYY-MM-DD", "YYYY-MM-DD")
