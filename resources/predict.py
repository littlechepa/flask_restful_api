from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt import jwt_required
import pandas as pd
import joblib

linear_regression_model = joblib.load('linear_regression_model.pkl')

class Prediction(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('avg_session_length',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('time_on_app',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('time_on_website',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('length_of_membership',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def post(self):
        data = Prediction.parser.parse_args()
        #dataa = pd.DataFrame(data=data,columns=[''])
        pred = linear_regression_model.predict([[data['avg_session_length'], data['time_on_app'], data['time_on_website'], data['length_of_membership']]])
        return jsonify(performance = pred[0])

