import sqlite3

conn = sqlite3.connect('sales.db')

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY,
    item TEXT,
    cost_price REAL,
    quantity INTEGER
    )"""
)

conn.commit()

print('successful')

inventory_list = [(1, 'pencil', 1.99, 95),
                (2, 'binder', 19.99, 50),
                (3, 'pen', 19.99, 27),
                (4, 'desk', 125.00, 2),
                (5, 'marker', 2.99, 90),
                (6, 'spiral notebook', 4.99, 29),
                (7, 'copy paper', 19.00, 35),
                (8, 'file folder', 1.99, 60),
                (9, 'letter envelope', 1.00, 27),
                (10, 'ink', 8.99, 56)]

print('successful')

cursor.executemany("INSERT INTO inventory VALUES(?, ?, ?, ?)", inventory_list)

conn.commit()

print('successful')

items = cursor.execute("""SELECT * 
                        FROM inventory
                        ORDER BY cost_price DESC""")

for row in items:
    print(row)