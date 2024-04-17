# Configuration settings and environment variables
from dotenv import load_dotenv
import os

# # Load the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

garmin_email = os.getenv('GARMIN_EMAIL')
garmin_password = os.getenv('GARMIN_PASSWORD')

db_host = os.getenv('DB_HOST')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_schema = os.getenv('DB_SCHEMA')
db_port = os.getenv('DB_PORT')


# print(db_host, db_username, db_password, db_name, db_port, db_schema)
