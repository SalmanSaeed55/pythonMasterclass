import sqlite3

conn = sqlite3.connect('./sqlite3_dbs/contacts.sqlite3')

name = input("Please enter a name to search? ")

for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()