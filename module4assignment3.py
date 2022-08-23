import sqlite3

conn = sqlite3.connect('students.db')

c = conn.cursor()

c.execute(
    """
    CREATE TABLE students_data(
    first_name TEXT,
    last_name TEXT,
    email TEXT
    )"""
)

conn.commit()

print('successful')

students_list = [('Will', 'Johnson', 'willjohnson@stutern.com'),
                ('John', 'Smith', 'johnsmith@stutern.com'),
                ('Katy', 'Brown', 'katybrown@stutern.com'),
                ]

c.executemany("INSERT INTO students_data VALUES(?, ?, ?)", students_list)

conn.commit()

print('successful')

c.execute("SELECT * FROM students_data")

items = c.fetchall()
print('FIRST NAME', '\t\tLAST NAME', '\t\tEMAIL')
print('----------', '\t\t---------', '\t\t-----')

for item in items:
    print(item[0], '\t\t\t', item[1], '\t\t\t', item[2])

conn.commit()

# Alter table name
c.execute("""ALTER TABLE students_data
            RENAME TO learners_info """)

conn.commit()

# Add new column
c.execute("""ALTER TABLE learners_info
            ADD COLUMN course """)

# Add values to new column
c.execute("""UPDATE learners_info 
            SET course = 'data_science'""")

conn.commit()

c.execute("SELECT * FROM learners_info")

items = c.fetchall()
print('FIRST NAME', '\t\tLAST NAME', '\t\tEMAIL', '\t\t\t\tCOURSE')
print('----------', '\t\t---------', '\t\t-----', '\t\t\t\t------')

for item in items:
    print(item[0], '\t\t\t', item[1], '\t\t', item[2], '\t\t', item[3])