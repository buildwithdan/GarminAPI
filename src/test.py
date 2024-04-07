from config import *
from models import *
from extract import info3

# # creating tables = working
# create_all_tables()

# Extract and Transform not needed = working
# print(info3)


engine = create_engine('mssql+pyodbc://r00t:password@dnell.database.windows.net/PrivateDB?driver=ODBC+Driver+17+for+SQL+Server;Connect Timeout=30')
