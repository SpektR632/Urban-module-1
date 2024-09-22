import sqlite3

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}gmail.com", f"{i*10}", f"{1000}"))
# cursor.execute("UPDATE Users SET balance = ? WHERE id%2 = 1", (f"500",))
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("DELETE FROM Users WHERE id = 6")
# users = cursor.fetchall()
# for id, name, email, age, balance in users:
#     print(f"Имя: {name}| Почта: {email}| Возраст: {age}| Баланс: {balance}")

cursor.execute("SELECT COUNT(*) FROM Users")
count_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]

print(total_balance / count_users, avg_balance)



connection.commit()
connection.close()