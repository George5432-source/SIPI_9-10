import os
from streamlit.testing.v1 import AppTest

def get_page1_app():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pages", "page1.py"))
    at = AppTest.from_file(path)
    at.run()
    return at

def test_input_values_set_correctly():
    at = get_page1_app()
    at.number_input[0].set_value(3)
    at.number_input[1].set_value(10)
    at.number_input[2].set_value(2)
    at.number_input[3].set_value(45.0)
    at.number_input[4].set_value(10.0)

    assert at.number_input[0].value == 3
    assert at.number_input[1].value == 10
    assert at.number_input[2].value == 2
    assert at.number_input[3].value == 45.0
    assert at.number_input[4].value == 10.0

def test_model_prediction_output():
    at = get_page1_app()
    at.number_input[0].set_value(3)
    at.number_input[1].set_value(10)
    at.number_input[2].set_value(2)
    at.number_input[3].set_value(45.0)
    at.number_input[4].set_value(10.0)

    for btn in at.button:
        if "🔍" in btn.label:
            btn.click()
            break

    at.run()
    expected_price = "💰 Предсказанная цена: **5 960 000 рублей**"
    assert any(success.value.strip() == expected_price for success in at.success), \
        f"Ожидали: {expected_price}, но не нашли в success-элементах"

def test_model_accuracy_output():
    at = get_page1_app()
    at.number_input[0].set_value(3)
    at.number_input[1].set_value(10)
    at.number_input[2].set_value(2)
    at.number_input[3].set_value(45.0)
    at.number_input[4].set_value(10.0)

    for btn in at.button:
        if "🔍" in btn.label:
            btn.click()
            break

    at.run()
    expected_accuracy = "✅ Точность: R² = 0.87 (на тестовой выборке)"
    assert any(info.value.strip() == expected_accuracy for info in at.info), \
        f"Ожидали: {expected_accuracy}, но не нашли в info-элементах"

def test_model_name_output():
    at = get_page1_app()
    at.number_input[0].set_value(3)
    at.number_input[1].set_value(10)
    at.number_input[2].set_value(2)
    at.number_input[3].set_value(45.0)
    at.number_input[4].set_value(10.0)

    for btn in at.button:
        if "🔍" in btn.label:
            btn.click()
            break

    at.run()
    assert any(info.value.strip() == "📈 Модель: LightGBM Regressor v1.0" for info in at.info), \
        "Ожидали вывод модели 'LightGBM Regressor v1.0', но не нашли"



def test_page3_distribution_plots():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pages", "page3.py"))
    at = AppTest.from_file(path)
    at.run()

    expected_subheaders = [
        "Распределение для столбца:",
        "Распределение по различным характеристикам",
    ]

    found_texts = [el.value for el in at.subheader]

    for expected in expected_subheaders:
        assert any(expected in text for text in found_texts), f"Подзаголовок '{expected}' не найден"
