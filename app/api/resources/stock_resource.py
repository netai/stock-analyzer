from flask_restful import Resource
from ..util.decorator import admin_token_required, token_required
from ..util.dto import StockDto, StockReportDto
from ..helpers.stock_helper import save_new_stock, get_all_stock, get_a_stock, get_report
from ..schema import ErrorSchema

class StockList(Resource):
    @token_required
    def get(self):
        """List all added stocks"""
        stock_list = get_all_stock()
        try:
            stocks = []
            for row in stock_list:
                stocks.append({
                    'id': row.id,
                    'symbol': row.symbol,
                    'company_name': row.company_name,
                    'series': row.series,
                    'listing_date': str(row.listing_date),
                    'isin_number': row.isin_number,
                    'face_value': row.face_value,
                    'company_detail': row.company_detail,
                    'company_website': row.company_website,
                    'exchange_name': row.exchange_name
                })
            respoonse_object = {
                'status': 'success',
                'data': {
                    'stocks': stocks
                }
            }
            return respoonse_object, 200
        except Exception as e:
            return ErrorSchema.get_response('InternalServerError', e)

    @admin_token_required
    def post(self):
        """add a new stock"""
        stock_request = StockDto.parser.parse_args()
        return save_new_stock(data=stock_request)

class Stock(Resource):
    @token_required
    def get(self, public_id):
        """get a stock detail"""
        stock_detail = get_a_stock(public_id)
        stock_detail_json = {
            'id': stock_detail.Stock.id,
            'symbol': stock_detail.Stock.symbol,
            'company_name': stock_detail.Stock.company_name,
            'series': stock_detail.Stock.series,
            'listing_date': str(stock_detail.Stock.listing_date),
            'isin_number': stock_detail.Stock.isin_number,
            'face_value': stock_detail.Stock.face_value,
            'company_detail': stock_detail.Stock.company_detail,
            'company_website': stock_detail.Stock.company_website,
            'exchange_name': stock_detail.Stock.exchange_name,
            'stock_report': {
                'date': str(stock_detail.StockReport.date),
                'prev_price': stock_detail.StockReport.prev_price,
                'open_price': stock_detail.StockReport.open_price,
                'high_price': stock_detail.StockReport.high_price,
                'low_price': stock_detail.StockReport.low_price,
                'last_price': stock_detail.StockReport.last_price,
                'close_price': stock_detail.StockReport.close_price,
                'avg_price': stock_detail.StockReport.avg_price,
                'traded_qty': stock_detail.StockReport.traded_qty,
                'delivery_qty': stock_detail.StockReport.delivery_qty,
                'delivery_per': round((stock_detail.StockReport.delivery_qty/stock_detail.StockReport.traded_qty)*100, 2),
                'change_per': round((abs(stock_detail.StockReport.prev_price-stock_detail.StockReport.last_price)/stock_detail.StockReport.prev_price)*100, 2)
            }
        }
        response_object = {
            'status': 'success',
            'data': {
                'stock': stock_detail_json
            }
        }
        return response_object, 200


class StockReport(Resource):
    @token_required
    def get(self, public_id):
        """get a stock report detail"""
        stock_report_request = StockReportDto.parser.parse_args()
        stock_report_detail = get_report(public_id, stock_report_request)
        stock_detail_json = []
        if stock_report_detail:
            for row in stock_report_detail:
                stock_detail_json.append({
                    'date': str(row.date),
                    'prev_price': row.prev_price,
                    'open_price': row.open_price,
                    'high_price': row.high_price,
                    'low_price': row.low_price,
                    'last_price': row.last_price,
                    'close_price': row.close_price,
                    'avg_price': row.avg_price,
                    'traded_qty': row.traded_qty,
                    'delivery_qty': row.delivery_qty,
                    'delivery_per': round((row.delivery_qty/row.traded_qty)*100, 2),
                })

        response_object = {
            'status': 'success',
            'data': {
                'stock_report': stock_detail_json
            }
        }
        return response_object, 200