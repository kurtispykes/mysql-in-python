import os

from mysql import connector
from dotenv import load_dotenv

# Access environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

"""PART 2: CREATING A NEW DATABASE """
try: 
    # Connect to server
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD
    ) as database: 
        
        # Create a database
        # Uncomment the code to delete db when executing multiple times
        # It will delete the previously created database. 
        # This means the remainder of the code recreates a new one. 
        delete_db = "DROP DATABASE book_ratings"
        create_db = "CREATE DATABASE book_ratings"
        with database.cursor() as cursor: 
            cursor.execute(delete_db) 
            cursor.execute(create_db)

            # Display existing databases
            show_existing_db = "SHOW DATABASES"
            cursor.execute(show_existing_db)
            for db in cursor:
                print(db)
# Catch errors
except connector.Error as e:
    print(e)


""" PART 2.1: CONNECTING TO AN EXISTING DATABASE"""
try:
    # Connect to server
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings" # The difference! 
    ) as database:
        
        print(f"Existing Database Object: {database}")

except connector.Error as e: 
    print(e)