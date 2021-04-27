from sqlite3 import connect

"""
1)
Create a zoo database with a table animal. 
Insert some animals, update the information, and delete som animals

2)
Add a table ‘animal_groups’. 
Relate the animal table to the animal_groups table.
"""

with connect('db/zoo.db') as conn:
    cur = conn.cursor()

    print('Dropping tables')
    cur.execute('DROP TABLE IF EXISTS animals')
    cur.execute('DROP TABLE IF EXISTS animal_groups')

    print('Creating tables and inserting data..')
    cur.execute('CREATE TABLE animal_groups(group_id integer PRIMARY KEY, group_name text)')
    cur.execute('INSERT INTO animal_groups (group_name) VALUES ("Lion"), ("Penguin"), ("Giraffe")')
    cur.execute('CREATE TABLE animals(animal_id integer PRIMARY KEY, group_id integer, animal_name text, FOREIGN KEY (group_id) REFERENCES animal_groups (group_id))')
    cur.execute('INSERT INTO animals (animal_name, group_id) VALUES ("Marty", 1), ("Pingu", 2), ("Melman", 3)')
    for i in cur.execute('SELECT * FROM animals'):
        print(i)

    print('Updating data..')
    cur.execute('UPDATE animals SET animal_name = "John" WHERE animal_id=1')

    for i in cur.execute('SELECT * FROM animals'):
        print(i)

    print('Deleting row..')
    cur.execute('DELETE FROM animals WHERE animal_id=3')

    for i in cur.execute('SELECT * FROM animals'):
        print(i)

    print('Joining animals and animal_groups')
    for i in cur.execute('SELECT animal_id, animal_name, group_name FROM animals INNER JOIN animal_groups ON animal_groups.group_id = animals.group_id'):
        print(i)

    print('Dropping tables')
    cur.execute('DROP TABLE animals')
    cur.execute('DROP TABLE animal_groups')