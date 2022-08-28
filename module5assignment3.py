import sqlite3

conn = sqlite3.connect('sales.db')

cursor = conn.cursor()

# Calculate the amount the business owner invested in the procurement of the items.
cursor.execute("""SELECT SUM((cost_price*quantity)) 
                FROM inventory""")

# Calculate the average quantity of items in stock.
cursor.execute("""SELECT AVG(quantity) 
                FROM inventory""")

# Determine the item with the least quantity in stock
cursor.execute("""SELECT item FROM inventory
                WHERE quantity = 
                (SELECT MIN(quantity) FROM inventory)""")

# Determine the item with the most quantity in stock
cursor.execute("""SELECT item FROM inventory
                WHERE quantity = 
                (SELECT MAX(quantity) FROM inventory)""")
                
items = cursor.fetchall()

for item in items:
    print(item)
