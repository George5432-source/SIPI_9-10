import streamlit as st
import numpy as np
import pandas as pd

COLUMNS = ["price", "level", "levels", "rooms", "area", "kitchen_area"]
if not st.session_state.get("conditions"):
    st.session_state.conditions = []

st.title("Фильтр квартир")

st.header("Введите условия для квартир")

button_col1, button_col2, button_col3 = st.columns(3)

with button_col1:
    if st.button('Добавить условие'):
        st.session_state.conditions.append(("price", ">", 0.0))

with button_col2:
    if st.button("Очистить условия"):
        st.session_state.conditions.clear()


for i, cond in enumerate(st.session_state.conditions):
    with st.expander(f"{cond[0]} {cond[1]} {cond[2]}"):
        with st.form(f'Condition {i}'):
            col1, col2, col3 = st.columns(3)
            with col1:
                field = st.selectbox("Выберите поле:", COLUMNS)
            with col2:
                op = st.selectbox("Выберите оператор:", [">", "<", "=", ">=", "<="])
            with col3:
                value = st.number_input("Введите значение:")
            
            with col1:
                if st.form_submit_button('Сохранить'):
                    st.session_state.conditions[i] = (field, op, value)
            with col2:
                if st.form_submit_button("Удалить"):
                    st.session_state.conditions.pop(i)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])


with button_col3:
    if st.button("Найти квартиры"):
        st.dataframe(chart_data)


