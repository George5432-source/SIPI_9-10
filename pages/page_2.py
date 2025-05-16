
import streamlit as st
import pandas as pd
import sqlite3
import os

# --- Константы ---
COLUMNS = ["price", "level", "levels", "rooms", "area", "kitchen_area"]
OPERATORS = {
    "=": lambda df, col, val: df[col] == val,
    ">": lambda df, col, val: df[col] > val,
    "<": lambda df, col, val: df[col] < val,
    ">=": lambda df, col, val: df[col] >= val,
    "<=": lambda df, col, val: df[col] <= val,
}

# --- Путь к базе данных ---
DB_PATH = os.path.join("D:/6-ой сем/ПоргКринж", "flats.db")

# --- Загрузка данных с фильтрацией ---
def load_filtered_data(query: str, params: list):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

# --- Состояние условий ---
if "conditions" not in st.session_state:
    st.session_state.conditions = []

st.title("Фильтр квартир")
st.subheader("Добавьте условия для фильтрации")

# --- Кнопки управления условиями ---
button_col1, button_col2, button_col3 = st.columns(3)

with button_col1:
    if st.button("➕ Добавить условие"):
        st.session_state.conditions.append(("price", ">", 0.0))

with button_col2:
    if st.button("🗑 Очистить условия"):
        st.session_state.conditions.clear()

# --- Отображение условий ---
for i, cond in enumerate(st.session_state.conditions):
    with st.expander(f"{cond[0]} {cond[1]} {cond[2]}"):
        with st.form(f"form_{i}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                field = st.selectbox("Поле", COLUMNS, index=COLUMNS.index(cond[0]), key=f"field_{i}")
            with col2:
                op = st.selectbox("Оператор", list(OPERATORS.keys()), index=list(OPERATORS.keys()).index(cond[1]), key=f"op_{i}")
            with col3:
                value = st.number_input("Значение", value=float(cond[2]), key=f"value_{i}")

            save_col, delete_col = st.columns(2)
            with save_col:
                if st.form_submit_button("💾 Сохранить"):
                    st.session_state.conditions[i] = (field, op, value)
            with delete_col:
                if st.form_submit_button("❌ Удалить"):
                    st.session_state.conditions.pop(i)

# --- Поиск по условиям ---
with button_col3:
    filter = st.button("🔍 Найти квартиры")

if filter:
        query = "SELECT * FROM flats WHERE 1=1"
        params = []

        for field, op, value in st.session_state.conditions:
            query += f" AND {field} {op} ?"
            params.append(value)

        # Установка лимита на количество строк, которое можно выбрать
        limit = st.number_input("Введите количество строк для отображения", min_value=1, value=10, step=1)

        try:
            filtered_df = load_filtered_data(query, params)
            # Применяем лимит
            filtered_df = filtered_df.head(limit)
            st.subheader(f"Найдено квартир: {len(filtered_df)}")
            st.dataframe(filtered_df, use_container_width=True)
        except Exception as e:
            st.error(f"Ошибка при фильтрации: {e}")

