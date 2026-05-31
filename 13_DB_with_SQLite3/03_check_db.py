import sqlite3
conn = sqlite3.connect('./sqlite3_dbs/contacts.sqlite3')

update_cursor = conn.cursor()
new_email = "master@update.com"
phone = 123456789
update_query = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_query)

update_cursor.execute(update_query, (new_email, phone))

for row in conn.execute('SELECT * FROM contacts'):
    print(row)

conn.close()