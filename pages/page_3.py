import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import os
import seaborn as sns
import matplotlib.pyplot as plt

# --- Путь к базе данных ---
DB_PATH = os.path.join("C:/Users/admin/Documents/MIREA_U/sipi", "flats.db")

# --- Функция для загрузки данных ---
def load_data(limit=1000):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT price, level, levels, rooms, area, kitchen_area FROM flats LIMIT {limit}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# --- Загрузка случайной выборки данных ---
df = load_data(limit=1000)  # Берем 1000 случайных строк для анализа

# --- Заголовок ---
st.title("Визуализация распределений характеристик квартир")

# --- Выбор столбца для анализа ---
COLUMNS = ["price", "level", "levels", "rooms", "area", "kitchen_area"]
selected_col = st.selectbox("Выберите столбец для визуализации:", COLUMNS)

# --- Определение графиков распределений ---
st.subheader(f"Распределение для столбца: {selected_col}")

# Строим гистограмму для выбранного столбца
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df[selected_col], kde=True, ax=ax)
ax.set_title(f"Распределение {selected_col}", fontsize=14)
ax.set_xlabel(selected_col, fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
st.pyplot(fig)

# --- Диаграмма распределения для других характеристик ---
st.subheader("Распределение по различным характеристикам")

# Гистограмма для цен
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df['price'], kde=True, ax=ax, color='green')
ax.set_title("Распределение цен", fontsize=14)
ax.set_xlabel("Цена", fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
st.pyplot(fig)

# Гистограмма для площади
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df['area'], kde=True, ax=ax, color='blue')
ax.set_title("Распределение площади", fontsize=14)
ax.set_xlabel("Площадь (м²)", fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
st.pyplot(fig)

# Диаграмма для количества комнат
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x=df['rooms'], ax=ax, palette='Set2')
ax.set_title("Распределение по количеству комнат", fontsize=14)
ax.set_xlabel("Количество комнат", fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
st.pyplot(fig)


st.write("Минимальная цена:", df['price'].min())
st.write("Максимальная цена:", df['price'].max())
st.write("Тип данных price:", df['price'].dtype)
