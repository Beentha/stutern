import sqlite3
import csv

conn = sqlite3.connect('waec.db')

cursor = conn.cursor()

student_table = """CREATE TABLE IF NOT EXISTS waecscore_data(
                    name TEXT,
                    mathematics INTEGER,
                    english INTEGER,
                    physics INTEGER,
                    chemistry INTEGER,
                    biology INTEGER,
                    further_mathematics INTEGER,
                    economics INTEGER,
                    civic_education INTEGER,
                    technical_drawing INTEGER
                    )"""

cursor.execute(student_table)

with open('waecscore_data.csv', 'r') as opened_file:
    read_file = csv.reader(opened_file)
    cursor.executemany("""
                        INSERT INTO waecscore_data 
                        VALUES (?,?,?,?,?,?,?,?,?,?)
                        """, read_file)

print("Successfully executed")

conn.commit()

# Query the table

# Which student scored the highest in maths
cursor.execute("""SELECT name FROM waecscore_data 
WHERE mathematics = 
(SELECT MAX(mathematics) FROM waecscore_data)""")

# Which student scored the lowest in english
cursor.execute("""SELECT name FROM waecscore_data 
WHERE english = 
(SELECT MIN(english) FROM waecscore_data)""")

# What is the average score of students in maths
cursor.execute("SELECT ROUND(AVG(mathematics)) FROM waecscore_data")

# What is the average score of students in english
cursor.execute("SELECT ROUND(AVG(english)) FROM waecscore_data")

# Who is the best performing student across all nine subjects in terms of overall scores
cursor.execute("""SELECT name FROM waecscore_data 
WHERE (mathematics + english + physics + chemistry + 
biology + further_mathematics + economics + civic_education + technical_drawing) = 
(SELECT MAX(mathematics + english + physics + chemistry + 
biology + further_mathematics + economics + civic_education + technical_drawing) 
FROM waecscore_data)""")

# Who is the best performing student across all nine subjects in term of average scores
cursor.execute("""SELECT name FROM waecscore_data 
WHERE ((mathematics + english + physics + chemistry + 
biology + further_mathematics + economics + civic_education + technical_drawing)/9) = 
(SELECT MAX(((mathematics + english + physics + chemistry + 
biology + further_mathematics + economics + civic_education + technical_drawing)/9)) 
FROM waecscore_data)""")

items = cursor.fetchall()

for item in items:
    print(item)
