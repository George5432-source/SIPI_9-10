import streamlit as st
from flat_model import predict_price, get_model_name, get_model_accuracy

st.title("Предсказание стоимости квартиры")

level = st.number_input("Этаж", value=3)
levels = st.number_input("Всего этажей", value=10)
rooms = st.number_input("Количество комнат", value=2)
area = st.number_input("Общая площадь (м²)", value=45.0)
kitchen_area = st.number_input("Площадь кухни (м²)", value=10.0)

if st.button("🔍 Предсказать цену"):
    st.write("Кнопка нажата ✅")
    params = {
        "level": level,
        "levels": levels,
        "rooms": rooms,
        "area": area,
        "kitchen_area": kitchen_area
    }
    price = predict_price(params)
    model_name = get_model_name()
    accuracy = get_model_accuracy()

    st.success(f"💰 Предсказанная цена: **{price}**")
    st.info(f"📈 Модель: {model_name}")
    st.info(f"✅ Точность: {accuracy}")
