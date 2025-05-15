# flat_model.py

def predict_price(params: dict) -> str:
    """
    Мок-функция для предсказания стоимости квартиры по параметрам.
    Параметры:
        params (dict): {
            "level": int,
            "levels": int,
            "rooms": int,
            "area": float,
            "kitchen_area": float
        }
    Возвращает:
        str: Предсказанная цена в формате строки (например, "12 350 000 рублей")
    """

    # Мок-логика: например, простая линейная комбинация + смещение
    base_price = (
        100000 * params.get("rooms", 1) +
        120000 * params.get("area", 30) +
        50000 * params.get("kitchen_area", 10) -
        20000 * (params.get("levels", 10) - params.get("level", 3))
    )

    # Ограничим в пределах разумного
    final_price = max(3_000_000, min(int(base_price), 50_000_000))

    return f"{final_price:,}".replace(",", " ") + " рублей"


def get_model_name() -> str:
    """
    Возвращает название модели
    """
    return "LightGBM Regressor v1.0"


def get_model_accuracy() -> str:
    """
    Возвращает строковое представление точности модели
    """
    return "R² = 0.87 (на тестовой выборке)"
