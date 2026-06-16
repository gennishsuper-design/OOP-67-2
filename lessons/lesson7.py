import sqlite3


# A4
connect = sqlite3.connect('user.db')
# Рука и карандаш
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()



# CRUD - Create, Read, Update, Delete