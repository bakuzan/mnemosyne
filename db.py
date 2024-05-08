import sqlite3
import os

def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row # Make query results dict rather than tuple
    except IOError as e:
        print(e)

    return conn 

## Fetch queries
def fetch_locations():
    """
    Query rows in the Locations table
    :return: Locations[]
    """   
    database = os.getenv("DATABASE_PATH")
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM Locations")
    return cur.fetchall()

def fetch_blacklist(locationId):
    """
    Query rows in the Blacklist table for a locationId
    :param locationId: location Id
    :return: Blacklist[]
    """
    database = os.getenv("DATABASE_PATH")
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM Blacklist WHERE LocationId IS NULL OR LocationId = ?", (locationId,))
    return cur.fetchall()

def fetch_whitelist(locationId):
    """
    Query rows in the Whitelist table for a locationId
    :param locationId: location Id
    :return: Whitelist[]
    """
    database = os.getenv("DATABASE_PATH")
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM Whitelist WHERE LocationId IS NULL OR LocationId = ?", (locationId,))
    return cur.fetchall()