import sqlite3

db = sqlite3.connect("./sqlite3_dbs/contacts.sqlite3")

db.execute("""CREATE TABLE IF NOT EXISTS contacts
              (
                  name  TEXT,
                  phone INTEGER,
                  email TEXT
               )""")
db.execute("""INSERT INTO contacts (name, phone, email)
                VALUES ('Salman', 123456789, 'salman@example.com')""")
db.execute("""INSERT INTO contacts (name, phone, email)
              VALUES ('Alex', 485673439, 'alex@example.com')""")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
for name, phone, email in cursor:
    print(name, phone, email, sep='\t')

cursor.close()
db.commit()
db.close()
