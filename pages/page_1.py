import streamlit as st

st.title("Предсказание цены квартиры")

with st.form("input_data"):
    st.subheader("Введите парамтеры жилого опомещения")
    input_param_1 = st.text_input("Введите значение: этаж квартиры")
    input_param_2 = st.text_input("Введите значение: количеcтво этажей в здании")
    input_param_3 = st.text_input("Введите значение: количеcтво комнат в квартире")
    input_param_4 = st.text_input("Введите значение: площадь квартиры (в квадратных метрах)")
    input_param_5 = st.text_input("Введите значение: площадь кухни (в квадратных метрах)")


    # Every form must have a submit button.
    submitted = st.form_submit_button("Посчитать цену")
    if submitted:
        st.write("Прогноз: тут будет прогноз")
        st.write("Метрики:")
        st.write("Тут будут метрики")
