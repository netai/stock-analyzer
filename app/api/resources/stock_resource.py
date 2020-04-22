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
        print(stock_detail)
        stock_detail_json = {
            'id': stock_detail.Stock.id,
            'symbol': stock_detail.Stock.symbol,
            'company_name': stock_detail.Stock.company_name,
            'series': stock_detail.Stock.series,
            'listing_date': str(stock_detail.Stock.listing_date),
            'isin_number': stock_detail.Stock.isin_number,
            'face_value': stock_detail.Stock.face_value,
            'company_detail': stock_detail.Stock.company_detail,
            'comapany_website': stock_detail.Stock.company_website,
            'trade_detail': {
                'nse': {
                    'date': str(stock_detail.StockReport.date),
                    'open_price': stock_detail.StockReport.open_price,
                    'high_price': stock_detail.StockReport.high_price,
                    'low_price': stock_detail.StockReport.low_price,
                    'last_price': stock_detail.StockReport.last_price,
                    'close_price': stock_detail.StockReport.close_price,
                    'avg_price': stock_detail.StockReport.avg_price,
                    'traded_qty': stock_detail.StockReport.traded_qty,
                    'dlvry_qty': stock_detail.StockReport.delivery_qty,
                    'dlvry_per': round((stock_detail.StockReport.delivery_qty/stock_detail.StockReport.traded_qty)*100, 2),
                }
            }
        }
        response_object = {
            'status': 'success',
            'data': {
                'stock': stock_detail_json
            }
        }
        return response_object, 200
