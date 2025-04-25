## 🔌 API Эндпоинты

### 📈 `POST /predict`

Предсказание цены квартиры

**Тело запроса (JSON):**
```json
{
  "level": 3,
  "levels": 9,
  "rooms": 2,
  "area": 48.0,
  "kitchen_area": 10.0,
  "building_type": 1,
  "object_type": 2,
  "region_id": 101
}
```

**Пример ответа:**
```json
{
  "estimation": 145000.0,
  "+/-2": 10000.0,
  "mape": 12.5
}
```

---

### 🔍 `POST /search`

Поиск квартир по фильтрам

**Тело запроса:**
```json
{
  "features_name": ["rooms", "area"],
  "conditions": [">=", "<="],
  "value": [2, 60.0]
}
```

**Пример ответа:**
```json
{
  "level": [1, 2],
  "levels": [5, 10],
  "rooms": [2, 3],
  "area": [45.5, 60.0],
  "kitchen_area": [10.0, 12.5],
  "building_type": [1],
  "object_type": [2],
  "region_id": [101]
}
```

---

### 📊 `POST /visualize`

Визуализация данных по признаку

**Тело запроса:**
```json
{
  "feature_name": "area"
}
```

**Пример ответа:**
```json
{
  "feature": [5, 15, 25, 35]
}
```