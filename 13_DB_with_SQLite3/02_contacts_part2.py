import sqlite3

db = sqlite3.connect('./sqlite3_dbs/contacts.sqlite3')

new_email = "anotherupdate@update.com"
phone = 5432

update_sql = f'UPDATE contacts SET email = "{new_email}" WHERE name = "Salman"'
print(update_sql)
update_cursor = db.cursor()
update_cursor.executescript(update_sql)
print(f"{update_cursor.rowcount} rows updated")

for name, phone, email in db.execute('SELECT * FROM contacts'):
    print(name)
    print(phone)
    print(email)
    print()

update_cursor.close()
db.close()
