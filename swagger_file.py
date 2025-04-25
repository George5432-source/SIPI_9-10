from flask import Flask, request
from flask_restx import Api, Resource, fields
from typing import List, Dict

app = Flask(__name__)
api = Api(app, title='Flat Analytics & Prediction API', version='2.0', description='API for flat prediction, search and visualization')

# ------------------- Models -------------------

predict_input = api.model('PredictInput', {
    'level': fields.Integer,
    'levels': fields.Integer,
    'rooms': fields.Integer,
    'area': fields.Float,
    'kitchen_area': fields.Float,
    'building_type': fields.Integer,
    'object_type': fields.Integer,
    'region_id': fields.Integer,
})

predict_result = api.model('PredictResult', {
    'estimation': fields.Float,
    '+/-2': fields.Float(attribute='plus_minus_2'),
    'mape': fields.Float
})

search_input = api.model('SearchInput', {
    'features_name': fields.List(fields.String),
    'conditions': fields.List(fields.String),
    'value': fields.List(fields.Raw),
})

search_result = api.model('SearchResult', {
    'level': fields.List(fields.Integer),
    'levels': fields.List(fields.Integer),
    'rooms': fields.List(fields.Integer),
    'area': fields.List(fields.Float),
    'kitchen_area': fields.List(fields.Float),
    'building_type': fields.List(fields.Integer),
    'object_type': fields.List(fields.Integer),
    'region_id': fields.List(fields.Integer),
})

visual_input = api.model('VisualInput', {
    'feature_name': fields.String
})

visual_result = api.model('VisualResult', {
    'feature': fields.List(fields.Raw)
})

# ------------------- Business Logic Classes -------------------

class PricePredictionModel:
    def __init__(self):
        self.model = None  # Placeholder

    def load_model(self, path: str) -> bool:
        # Dummy model loading
        self.model = "Loaded model"
        return True

    def predict_price(self, input_data: Dict[str, any]) -> Dict[str, float]:
        return {
            'estimation': 145000.0,
            'plus_minus_2': 10000.0,
            'mape': 12.5
        }


class FlatPredictionData:
    def preprocess_input(self, data: Dict[str, any]) -> Dict[str, any]:
        return data  # Add preprocessing if needed

    def validate_conditions(self, data: Dict[str, any]) -> bool:
        return True  # Add validation logic


class Database:
    def connect(self) -> bool:
        return True  # Fake connection

    def query(self, sql: str, params: List[any]) -> List[Dict]:
        return []  # Fake result


class FlatSearchData:
    def __init__(self):
        self.database = Database()

    def filter_flats(self, criteria: Dict[str, any]) -> Dict[str, List]:
        return {
            'level': [1, 2],
            'levels': [5, 10],
            'rooms': [2, 3],
            'area': [45.5, 60.0],
            'kitchen_area': [10.0, 12.5],
            'building_type': [1],
            'object_type': [2],
            'region_id': [101]
        }


class FlatAnalytics:
    def __init__(self):
        self.database = Database()

    def generate_statistics(self) -> Dict[str, List]:
        return {
            'feature': [10, 20, 30, 40]
        }

    def generate_diagram(self, metric: str) -> Dict[str, List]:
        return {
            'feature': [5, 15, 25, 35]
        }

# ------------------- Endpoints -------------------

model = PricePredictionModel()
model.load_model("fake_path.model")
predictor = FlatPredictionData()
searcher = FlatSearchData()
analytics = FlatAnalytics()


@api.route('/predict')
class Predict(Resource):
    @api.expect(predict_input)
    @api.marshal_with(predict_result)
    def post(self):
        data = request.json
        if not predictor.validate_conditions(data):
            api.abort(400, "Validation failed for input data")

        processed = predictor.preprocess_input(data)
        return model.predict_price(processed)


@api.route('/search')
class Search(Resource):
    @api.expect(search_input)
    @api.marshal_with(search_result)
    def post(self):
        data = request.json
        return searcher.filter_flats(data)


@api.route('/visualize')
class Visualize(Resource):
    @api.expect(visual_input)
    @api.marshal_with(visual_result)
    def post(self):
        feature = request.json.get("feature_name")
        return analytics.generate_diagram(feature)

# ------------------- Main -------------------

if __name__ == '__main__':
    app.run(debug=True)
