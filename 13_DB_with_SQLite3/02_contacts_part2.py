import sqlite3

db = sqlite3.connect('./sqlite3_dbs/contacts.sqlite3')

update_sql = 'UPDATE contacts SET email = "update@update.com" WHERE name = "Salman"'
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows updated")

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print()

db.close()
