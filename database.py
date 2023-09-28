import sqlite3


conn = sqlite3.connect('fridgeTemp.db')

#create cursor
c = conn.cursor()

#create a table
#c.execute("""CREATE TABLE dateAndTemp (temp real,date text)""")
#c.execute("""CREATE TABLE dateAndTemp1 (temp real,date text)""")

def addToDatabase(temp, date):
    c.execute("INSERT INTO dateAndTemp1 VALUES(temp, date)")
    print("command executed succesfully")

#addToDatabase(10.5,"Aug 10")

#addToDatabase(10.5,"Aug 10")

#commit
conn.commit()

#close Connection
conn.close()
