import sys
import sqlite3 as lite

# connect to the pets db
conn= lite.connect('thepets.db')

# raw_input for getting the user id
the_id= raw_input('Enter ID of person you would like to search: ')

with conn:
    cur = conn.cursor()
    while True:
        if (the_id == -1):
            print "Invalid"
            # sys.exit()

        cur.execute('SELECT person.first_name, person.last_name, person.age, pet.name, pet.age, pet.dead breed FROM person, pet, person_pet WHERE person.id=? AND person.id == person_pet.person_id AND person_pet.pet_id == pet.id',(the_id))
        scrape= cur.fetchall()
        print scrape
        break


conn.close()


#When I was wworking on this i needed to change the interpreter. I did this by going to File> Settings > Project Interpreter.
# Unknown Error: ...
# Run> Edit Configurations> Pick the conda interpreter (again)