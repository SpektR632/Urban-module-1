import sqlite3

connection = sqlite3.connect('initiate.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER NOT NULL)
''')

products = [('Банан', 'Вкусный, желтый', '100'), ('Апельсин', 'Сладкий, оранжевый', '200'),
            ('Киви', 'С кислинкой, зеленый', '300'), ('Авокадо', 'странный, можно в салатик', '400')]

# for product, description, price in products:
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (product, description, price))
connection.commit()
def get_all_products():
    cursor.execute('''
    SELECT * FROM Products
    ''')
    return cursor.fetchall()
print(get_all_products())
