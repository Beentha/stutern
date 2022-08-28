import sqlite3
import csv

conn = sqlite3.connect('celebs.db')

cursor = conn.cursor()

celebs_table = """CREATE TABLE IF NOT EXISTS celebrity_data(
                    name TEXT UNIQUE,
                    genre TEXT,
                    num_albums INTEGER,
                    age INTEGER,
                    awards INTEGER,
                    years_in_industry INTEGER
                    )"""

cursor.execute(celebs_table)

with open('celebrity.csv', 'r') as opened_file:
    read_file = csv.DictReader(opened_file)
    celebs_data = [(i['name'], i['genre'], i['num_albums'], 
    i['age'], i['awards'], i['years_in_industry']) for i in read_file]
    print("Celebs info successfully read")

    cursor.executemany("""
                        INSERT INTO celebrity_data 
                        VALUES (?,?,?,?,?,?)
                        """, celebs_data)

print("Successfully executed")

conn.commit()

# Query database

# Who is the most decorated celebrity?
cursor.execute("""SELECT name FROM celebrity_data
                WHERE awards = 
                (SELECT MAX(awards) FROM celebrity_data)""")

# Who is the oldest celebrity?
cursor.execute("""SELECT name FROM celebrity_data
                WHERE age = 
                (SELECT MAX(age) FROM celebrity_data)""")

# Which celebrity has been in the industry the longest?
cursor.execute("""SELECT name FROM celebrity_data
                WHERE years_in_industry = 
                (SELECT MAX(years_in_industry) FROM celebrity_data)""")

# Which celebrity has the least number of albums?
cursor.execute("""SELECT name FROM celebrity_data
                WHERE num_albums = 
                (SELECT MIN(num_albums) FROM celebrity_data)""")

# What is the most popular genre of music amongst all celebrities in the dataset?
cursor.execute("""SELECT genre FROM celebrity_data
                GROUP BY genre
                ORDER BY COUNT(genre) DESC
                LIMIT 1""")

items = cursor.fetchall()

for item in items:
    print(item)
