import os

from mysql import connector
from dotenv import load_dotenv

# Access environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

"""PART 6: WHERE"""
try:
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        condition = "SELECT author, title FROM books WHERE release_year <= 2010"
        with existing_database.cursor() as cursor:
            cursor.execute(condition)
            
            # Display returned data
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)
        
except connector.Error as e: 
    print(e)

"""PART 6.1: ORDER BY"""
try:
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        order_by_year = "SELECT * FROM books ORDER BY release_year DESC"
        with existing_database.cursor() as cursor:
            cursor.execute(order_by_year)
            
            # Display returned data
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)
        
except connector.Error as e: 
    print(e)

"""PART 6.2: LIMIT"""
try:
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        define_limit = "SELECT * FROM books LIMIT 3"
        with existing_database.cursor() as cursor:
            cursor.execute(define_limit)
            
            # Display returned data
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)
        
except connector.Error as e: 
    print(e)