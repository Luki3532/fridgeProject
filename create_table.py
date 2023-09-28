# create_table.py
import connect_db
def create_table():
    """
    Creates a table ready to accept our data.

    write code that will execute the given sql statement
    on the database
    """

    create_table = """ CREATE TABLE authors(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    pages INTEGER NOT NULL,
    due_date CHAR(15) NOT NULL
    )
    """

con = connect_db.get_database_connection()
con.execute(create_table)
con.close()

