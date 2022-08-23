import sqlite3
print("Module successfully imported")

conn = sqlite3.connect('SGA_1_3_learners.db')
print("Database successfully created")

cursor = conn.cursor()
print("Cursor created successfully")

# cursor.execute(
#     """
#     CREATE TABLE learners(
#         first_name text,
#         last_name text,
#         email text,
#         phone_number text
#     )
#     """)
# print("Table successfully created")

learners_list = [('Esther', 'Akpanowo', 'estherakpanowo@stutern.com', '09077546691'),
                ('Eke', 'Ihuoma', 'ekeihuoma@stutern.com', '09067547795'),
                ('Louis', 'Etariemi', 'louisetariemi@stutern.com', '09077546682'),
                ('Omowunmi', 'Awoniran', 'omowunmiawoniran@stutern.com', '08132958070'),
                ('Faith', 'Amure', 'faithamure@stutern.com', '08081396865'),
                ('Binta', 'Umar', 'bintaumar@stutern.com', '08027284588')
                ]

cursor.executemany("INSERT INTO learners VALUES(?, ?, ?, ?)", learners_list)
print("Inserted multiple records at once")

cursor.execute("SELECT * FROM learners")
print("Query successfully executed")

records = cursor.fetchall()

print("first_name", "\t last_name", "\t email", "\t\t\t\t phone_number \n" f"{'.' * 100}")

for record in records:
    first_name, last_name, email, phone_number = record
    print(f"{first_name:16}{last_name:16}{email}\t\t{phone_number}")

conn.commit()

conn.close()