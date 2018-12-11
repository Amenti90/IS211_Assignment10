import sqlite3 as lite
import sys

conn= lite.connect("thepets.db")
conn.execute(''' DROP TABLE IF EXISTS person;''')
conn.execute(''' DROP TABLE IF EXISTS pet;''')
conn.execute(''' DROP TABLE IF EXISTS person_pet;''')

conn. execute('''CREATE TABLE person(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER );''')

conn.execute('''CREATE TABLE pet(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER);''')

conn.execute('''CREATE TABLE person_pet(
    person_id INTEGER,
    pet_id INTEGER
    );''')


with conn:
    cur= conn.cursor()

    cur.execute("INSERT INTO person VALUES (1, 'James', 'Smith',41)")
    cur.execute("INSERT INTO person VALUES (2, 'Diana','Green', 23)")
    cur.execute("INSERT INTO person VALUES (3, 'Sara', 'White', 27)")
    cur.execute("INSERT INTO person VALUES (4, 'William', 'Gibson', 23)")
    cur.execute("INSERT INTO pet VALUES (1,'Rusty','Dalmation',4,5)")
    cur.execute("INSERT INTO pet VALUES (2,'Bella','Alaskan Malamute', 3,0)")
    cur.execute("INSERT INTO pet VALUES (3,'Max','Cocker Spaniel', 4,1)")
    cur.execute("INSERT INTO pet VALUES (4,'Rocky','Beagle', 7,0)")
    cur.execute("INSERT INTO pet VALUES (5,'Rufus','Cocker Spaniel', 1,0)")
    cur.execute("INSERT INTO pet VALUES (6,'Spot','Bloodhound', 2,1)")
    cur.execute("INSERT INTO person_pet VALUES (1,1)")
    cur.execute("INSERT INTO person_pet VALUES (1,2)")
    cur.execute("INSERT INTO person_pet VALUES (2,3)")
    cur.execute("INSERT INTO person_pet VALUES (2,4)")
    cur.execute("INSERT INTO person_pet VALUES (3,5)")
    cur.execute("INSERT INTO person_pet VALUES (4,6)")



conn.close()
































#
# conn = lite.connect('pets.db.sqlite')
# # cur.execute()
#
# with conn:
#     cur= conn.cursor()
#     cur.execute("INSERT INTO pet VALUES (1,'Audi')")
#
#
#







    # cur.execute('SELECT SQLITE_VERSION()')
    # data= cur.fetchone()
    # print ("SQLite version: {}".format(data))

# except lite.Error as e:
#     print ("Error {}:".format(e.args[0]))
#     sys.exit(1)
#
# finally:
#     if conn:
#         conn.close()





