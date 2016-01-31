# create a SQLite3 table and populate it with blog data

import sqlite3

#create a new database (if doesn't already exists)

with sqlite3.connect("blog.db") as connection:

	#create a cursor object
	c = connection.cursor()
	
	#create the table
	c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

	#insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	c.execute('INSERT INTO posts VALUES("Okay","I\'m okay.")')