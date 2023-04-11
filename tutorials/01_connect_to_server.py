import os

from mysql import connector
from dotenv import load_dotenv

# Access environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

"""PART 1: CONNECTING TO MYSQL SERVER"""

try:
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD
    ) as database: 
        print(f"Database object: {database}")
except connector.Error as e: 
    print(e)