import sqlite3

# 1. Подключаемся к базе данных (файл cinema.db создастся автоматически)
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

# ЧАСТЬ 1 — СОЗДАНИЕ ТАБЛИЦ И ЗАПОЛНЕНИЕ ДАННЫМИ

# Включаем поддержку внешних ключей в SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Удаляем таблицы, если они были, для чистого перезапуска
cursor.executescript('''
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER CHECK (rating >= 1 AND rating <= 10),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
);
''')

# Заполняем данными
users_data = [('Алексей',), ('Мария',), ('Иван',), ('Елена',), ('Дмитрий',)]
cursor.executemany("INSERT INTO users (name) VALUES (?);", users_data)

movies_data = [
    ('Интерстеллар', 'Научная фантастика'),
    ('Начало', 'Фантастика'),
    ('Зеленая миля', 'Драма'),
    ('Темный рыцарь', 'Боевик'),
    ('Скучный фильм 2026', 'Документальный')
]
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?);", movies_data)

reviews_data = [
    (1, 1, 10), (1, 2, 9),  (1, 3, 8),
    (2, 1, 9),  (2, 4, 10),
    (3, 2, 8),  (3, 3, 9),
    (4, 1, 9),  (4, 4, 7),
    (5, 2, 7),  (5, 3, 10)
]
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?);", reviews_data)
conn.commit()


# ЧАСТЬ 2 — JOIN

print("--- 1. Имя пользователя + Фильм + Оценка ---")
cursor.execute('''
SELECT u.name, m.title, r.rating
FROM reviews r
JOIN users u ON r.user_id = u.id
JOIN movies m ON r.movie_id = m.id;
''')
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]} | Фильм: {row[1]} | Оценка: {row[2]}")

print("\n--- 2. ВСЕ фильмы (даже без отзывов) ---")
cursor.execute('''
SELECT m.title, r.rating
FROM movies m
LEFT JOIN reviews r ON m.id = r.movie_id;
''')
for row in cursor.fetchall():
    print(f"Фильм: {row[0]} | Оценка: {row[1]}")


# ЧАСТЬ 3 — АГРЕГАЦИИ

print("\n--- 3. Статистика оценок ---")
cursor.execute('''
SELECT ROUND(AVG(rating), 1), MAX(rating), MIN(rating)
FROM reviews;
''')
stats = cursor.fetchone()
print(f"Средняя оценка: {stats[0]}")
print(f"Максимальная оценка: {stats[1]}")
print(f"Минимальная оценка: {stats[2]}")

# Закрываем соединение
conn.close()