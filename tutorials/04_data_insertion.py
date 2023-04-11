import os

from mysql import connector
from dotenv import load_dotenv

# Access environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

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