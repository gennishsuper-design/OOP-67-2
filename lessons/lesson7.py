import sqlite3

connect = sqlite3.connect('user.db')
cursor = connect.cursor()

# Создаём таблицу users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CREATE
def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print('пользователь создан')

# READ
def get_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)

# UPDATE
def update_user(name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )
    connect.commit()
    print('пользователь обновлен')

# DELETE
def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print('пользователь удален')

# === ТЕСТ ===
if __name__ == "__main__":
    create_user("Jarvan", 40, "Быть королем")
    get_users()