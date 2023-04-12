import os

from mysql import connector
from dotenv import load_dotenv

# Access environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

"""PART 7: UPDATING AND DELETING DATA"""

update_query = """
UPDATE
    books
SET
    author = "Big J" 
WHERE 
    author = "James Altucher"
"""

try:
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        with existing_database.cursor() as cursor:
            cursor.execute(update_query)
            existing_database.commit()
        
            # View author names
            select_author_names = "SELECT DISTINCT author FROM books"
            cursor.execute(select_author_names)

            # Display returned data
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)

except connector.Error as e:
    print(e)

"""PART 7.1: DELETE"""
try: 
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        drop_record = "DELETE FROM books WHERE release_year <= 2000"
        with existing_database.cursor() as cursor:
            cursor.execute(drop_record)
            existing_database.commit()
            
            # Display books years 
            unique_book_years = "SELECT DISTINCT release_year FROM books"
            cursor.execute(unique_book_years)
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)
except connector.Error as e: 
    print(e)

"""PART 7.2: DROP TABLE"""
try: 
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        drop_table = "DROP TABLE IF EXISTS books"
        with existing_database.cursor() as cursor:
            cursor.execute(drop_table)
            existing_database.commit()
except connector.Error as e: 
    print(e)