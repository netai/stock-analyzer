from flask_restful import Resource
import pandas as pd
from ..util.decorator import admin_token_required, token_required
from ..helpers.chart_pattern_helper import 

class ChartPatternIdentifire(Resource):
    @token_required
    def get(self, symbol):
        """Stock Chart Pattern identifier"""
        try:
            stock_data = get_stock_data_limit(symbol, 4)
            candle_pattern, candle_score = find_candle_pattern(stock_data)
            signal = 'NONE'
            if candle_score > 0:
                signal = 'UP'
            elif candle_score < 0:
                signal = 'DOWN'
            
            response_object = {
                'status': 'success',
                'data': {
                    'analyzer': {
                        'candle_pattern': candle_pattern,
                        'signal': signal
                    }
                }
            }
            return response_object, 200
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 500