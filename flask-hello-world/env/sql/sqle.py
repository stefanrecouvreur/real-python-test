#INSERT Command

#import the sqlite3 library
import sqlite3

#create the connection object
conn = sqlite3.connect("new.db")
cursor = conn.cursor()

try:
#insert data
    cursor.execute("INSERT INTO population VALUES('Marseille', 'NY', 8200000)")
    cursor.execute("INSERT INTO population VALUES('Dijon', 'CA', 8000000)")
    conn.commit()

except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again..."
	
conn.close()
		
		