import os

from mysql import connector
from dotenv import load_dotenv

# Access environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

"""PART 3: CREATING TABLES"""
create_books_table = """
CREATE TABLE books(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(100),
    release_year YEAR(4)
)
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
            cursor.execute(create_books_table)
            existing_database.commit()
        
            # Display the table schema 
            describe_books = "DESCRIBE books"
            cursor.execute(describe_books)
            books_schema = cursor.fetchall() 
            for column in books_schema: 
                print(column)

except connector.Error as e: 
    print(e)