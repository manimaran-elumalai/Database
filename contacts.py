import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Manimaran', 23776966, 'manimaran.ac@gmail.com')")
db.execute("INSERT INTO contacts Values('Christy', 23776966, 'christymanimaran@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Rahul', '+91 9710322807', 'rahul@gmail.com')")
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# for row in cursor:

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("**" * 5)

cursor.close()
db.commit()
db.close()