"""
    Online Booking sub-system: database driver code

    Handles the creation of the database and inserting the sample data for
    - movies
    - customers
    - bookings

    Changelog:
        28NOV2022 - Initial release

"""

import os
import sqlite3
from sqlite3 import Error
import pathlib

#pwd = pathlib.Path().absolute()  # current working folder
conn = None # databse conenction handle

def dbconnect(db):
    """ 
    Connect to the database
    :param db: databse folder location + datasbe name
    :return conn: database connection handle
    """

    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
        return None
    return conn

def prepareDB(conn):
    """ 
    Create the database for the website
    :param conn: database connection handle
    :return:
    """

    SQL = ["""
        CREATE TABLE IF NOT EXISTS customers (
            id integer PRIMARY KEY,
            name text NOT NULL,
            contact text NOT NULL,
            email text NOT NULL
        );
    """,
    """               
        CREATE TABLE IF NOT EXISTS movies (
            id integer PRIMARY KEY,
            name text NOT NULL,
            minutes integer NOT NULL,
            rating text NOT NULL,
            genre text NOT NULL           
        );           
    """,
    """
        CREATE TABLE IF NOT EXISTS bookings (
            id integer PRIMARY KEY,
            customerID integer NOT NULL,
            movieID integer NOT NULL,
            session integer NOT NULL                
        );           

    """]
    try:
        for s in SQL:
            db = conn.cursor()
            db.execute(s)
            conn.commit()
    except Error as e:
        print(e)
        
def importData(conn):
    """ import the sample data into the database
    :param conn: database connection handle
    :return:
    """

    MDATA = [
        ["The Shawshank Redemption", 142, "RP16", "Drama"],
        ["The Godfather", 175, "R16", "Action"],
        ["The Dark Knight", 152, "M", "Sci-Fi"],
        ["12 Angry Men", 96, "G", "Action"],
        ["Schindler's List", 195, "RP13", "not set"],
        ["The Lord of the Rings: The Return of the King", 201, "M", "not set"],
        ["One Flew Over the Cuckoo's Nest", 133, "R18", "not set"],
        ["The Lord of the Rings: The Fellowship of the Ring", 178, "PG", "not set"],
        ["Saving Private Ryan", 169, "R15", "not set"],
        ["Blade Runner 2049", 164, "R13", "not set"],
        ["Halloween", 91, "R16", "not set"],
        ["Beverly Hills Cop", 105, "RP16", "not set"],
        ["Platoon", 120, "RP16", "not set"],
        ["Total Recall", 113, "RP16", "not set"],
        ["Back to the Future", 116, "G", "not set"],
        ["The Lion King", 88, "G", "not set"],
        ["Cars", 117, "G", "not set"],
        ["The Wizard of Oz", 102, "G", "not set"],
        ["The Wolf of Wall Street", 180, "R18", "not set"],
        ["Harry Potter and the Philosopher's Stone", 152, "PG", "not set"],
        ["Poltergeist", 114, "not set", "not set"],
        ["Full Metal Jacket", 116, "RP13", "not set"],
        ["The Exorcist", 122, "R15", "not set"],
        ["Apocalypse Now", 147, "R16", "not set"],
    ]
    CDATA = [
        ["Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com"],
        ["Jane Doe", "021-456-4567", "jane.doe@mail.com"],
        ["King Kong", "021-123-4567", "king.kong@mail.com"],
        ["ABC", "022-123-1234", "ABC@mail.com"],
        ["DEF", "022-456-4567", "DEF@mail.com"],
        ["HIJ", "024-123-4567", "HIJ@mail.com"]
    ]
    BDATA = [
        [1,1,1],
        [2,2,23],
        [3,1,17],
        [3,2,21],
        [4,1,17],
        [5,2,17],
        [6,2,17]
    ]

    cur = conn.cursor()
    # import the movies
    for d in MDATA:
        cur.execute("INSERT INTO movies (name,minutes,rating,genre) VALUES(?,?,?,?)", (d[0],d[1],d[2],d[3]))
    conn.commit()
    
    # import the customers
    for d in CDATA:
        cur.execute("INSERT INTO customers (name,contact,email) VALUES(?,?,?)", (d[0],d[1],d[2]))
    conn.commit()

    # import the bookings
    for d in BDATA:
        cur.execute("INSERT INTO bookings (customerID,session,movieID) VALUES(?,?,?)", (d[0],d[1],d[2]))
    conn.commit()

    cur.close()

if __name__ == "__main__":
    db = os.getcwd()+"\cinema.db"
    print(f"Import data into {db}")
    if "cinema.db" in os.listdir():    
        print("- Removing existing database")
        os.remove(db)    

    conn = dbconnect(db)
    if conn:
        print("- creating tables")        
        prepareDB(conn)
        print("- importing data")                
        importData(conn)
    conn.close()
    print("Import complete") 
                 