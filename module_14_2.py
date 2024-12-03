import sqlite3

connection = sqlite3.connect('nott_telegram.db')
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
#cursor.execute(''' DELETE FROM Users''')
#cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#for i in range(1, 11):
    #cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))
#for i in range(1,11,2):
    #cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', ('500', f'{i}'))

#for i in range(1, 11, 3):
    #cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))

#cursor.execute('SELECT username, email, age, balance FROM Users WHERE age !=?', (60,) )
#users = cursor.fetchall()
#for user in users:
    #print(user)

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*)FROM Users')
total_users = cursor.fetchone()
print(total_users)
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()
print(all_balances)
#average_balance = int(all_balances)/int(total_users)
#print(all_balances, all_balances/total_users)
cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()
print(average_balance)

connection.commit()
connection.close()
