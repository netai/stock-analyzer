from flask_restful import Resource
from ..util.decorator import admin_token_required, token_required
from ..helpers.analyzer_helper import find_candle_pattern
from ..helpers.stock_helper import get_all_stock

class StockIndicator(Resource):
    @token_required
    def get(self, id):
        """Stock indicator and candle pattern finder"""
        """try:
            stock_data = get_stock_data_limit(id, 4)
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
            return response_object, 500"""

class StockListIndicator(Resource):
    @token_required
    def get(self):
        """Stock list indicator and candle pattern finder"""
        """try:
            candle_pattern_list = []
            stock_list = get_all_stock()
            for stock in stock_list:
                stock_data = get_stock_data_limit(stock.symbol, 4)
                candle_pattern, candle_score = find_candle_pattern(stock_data)
                signal = 'NONE'
                if candle_score > 0:
                    signal = 'UP'
                elif candle_score < 0:
                    signal = 'DOWN'
                candle_pattern_list.append({
                    'stock_id': stock.id,
                    'symbol': stock.symbol,
                    'candle_pattern': candle_pattern_list,
                    'signal': signal
                })
            
            response_object = {
                'status': 'success',
                'data': {
                    'analyzer': candle_pattern_list
                }
            }
            return response_object, 200
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 500"""
