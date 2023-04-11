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

# """PART 3: CREATING TABLES"""
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

"""PART 4: DATA INSERTION"""
# INSERT SINGLE RECORD
insert_single_record = "INSERT INTO books (id, title, author, genre, release_year)\
    VALUES (%s, %s, %s, %s, %s)"
single_record = (
    "1", "Choose Yourself! Be Happy, Make Millions, Live the Dream", "James Altucher", "self-help", "2013"
    )

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
            cursor.execute(insert_single_record, single_record)
            existing_database.commit()
        
except connector.Error as e: 
    print(e)

# INSERT MULTIPLE RECORDS
insert_multiple_records = "INSERT INTO books (id, title, author, genre, release_year)\
    VALUES (%s, %s, %s, %s, %s)"
multiple_records = [
    (
        "2", 
        "Skip the Line: The 10,000 Experiments Rule and Other Surprising Advice for Reaching Your Goals",
        "James Altucher",
        "self-help",
        "2021"        
    ),
    (
        "3",
        "The Power of No: Because One Little Word Can Bring Health, Abundance, and Happiness",
        "James Altucher",
        "self-help",
        "2014"
    ),
    (
        "4",
        "The 48 Laws of Power",
        "Robert Greene",
        "self-help",
        "1998"
    ),
    (
        "5",
        "Mastery",
        "Robert Greene",
        "self-help",
        "2012"
    ),
    (
        "6",
        "The Art of Seduction",
        "Robert Greene",
        "self-help",
        "2001"
    ),
]

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
            cursor.executemany(insert_multiple_records, multiple_records)
            existing_database.commit()
        
except connector.Error as e: 
    print(e)

"""PART 5: SELECTING DATA"""
# Select specific columns example
try: 
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        select_specific_cols = "SELECT author, release_year FROM books"
        with existing_database.cursor() as cursor:
            cursor.execute(select_specific_cols)
            
            # Display returned data
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)
        
except connector.Error as e: 
    print(e)

# Select all columns example
try:
    # Connect to existing database
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD,
        database = "book_ratings"
    ) as existing_database:
        
        # Create cursor object
        select_specific_cols = "SELECT * FROM books"
        with existing_database.cursor() as cursor:
            cursor.execute(select_specific_cols)
            
            # Display returned data
            returned_data = cursor.fetchall()
            for result in returned_data:
                print(result)
        
except connector.Error as e: 
    print(e)


"""PART 5.1: WHERE"""
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

"""PART 5.2: ORDER BY"""
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

"""PART 5.3: LIMIT"""
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

"""PART 6: UPDATING AND DELETING DATA"""

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

"""PART 6.2: DELETE"""
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

"""PART 6.3: DROP TABLE"""
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