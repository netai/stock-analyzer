from flask_restful import Resource, marshal, marshal_with
from ..util.decorator import admin_token_required, token_required
from ..util.dto import StockDto
from ..util.schema import StockSchema
from ..helpers.stock_helper import save_new_stock, get_all_stock, get_a_stock

class StockList(Resource):
    @token_required
    def get(self):
        """List all added stocks"""
        stock_list = get_all_stock()
        respoonse_object = {
            'status': 'success',
            'data': {
                'stocks': marshal(stock_list, StockSchema.stock_list)
            }
        }
        return respoonse_object, 200
    
    @admin_token_required
    def post(self):
        """add a new stock"""
        stock_request = StockDto.parser.parse_args()
        return save_new_stock(data=stock_request)

class Stock(Resource):
    @token_required
    def get(self, symbol):
        """get a stock given its identifier"""
        stock_detail = get_a_stock(symbol)
        response_object = {
            'status': 'success',
            'data': {
                'stock': stock_detail
            }
        }
        return response_object, 200
