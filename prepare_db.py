import sqlite3
import pandas as pd
import os

# Пути
CSV_PATH = "C:/Users/admin/Documents/MIREA_U/sipi/input_data.csv"
DB_PATH = "C:/Users/admin/Documents/MIREA_U/sipi/flats.db"

# Чтение CSV с указанием разделителя ";"
df = pd.read_csv(CSV_PATH, delimiter=";")

# Если база данных существует, удалим её, чтобы избежать конфликтов
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print(f"{DB_PATH} уже существовала и была удалена.")

# Подключение к SQLite и запись таблицы
try:
    with sqlite3.connect(DB_PATH) as conn:
        # Запись данных в таблицу "flats", если таблица существует, она будет заменена
        df.to_sql("flats", conn, if_exists="replace", index=False)
    print("База данных успешно создана:", DB_PATH)
except Exception as e:
    print(f"Ошибка при создании базы данных: {e}")
