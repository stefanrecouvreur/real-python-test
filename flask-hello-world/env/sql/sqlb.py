#INSERT Command

#import the sqlite3 library
import sqlite3

#create the connection object
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

#insert data
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    c.execute("INSERT INTO population VALUES('San Fransisco', 'CA', 8000000)")
