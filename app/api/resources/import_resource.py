from flask_restful import Resource
from ..util.decorator import admin_token_required
from ..helpers.import_helper import save_import_stock, save_history_report, save_daily_report, replace_import_symbol
from ..helpers.stock_helper import get_all_stock
from ..helpers.nse_helper import NSEHelper
from ..schema.error_schema import ErrorSchema

class ImportStock(Resource):
    @admin_token_required
    def get(self):
        """Import stocks from nse/bse website and store into database"""       
        try:
            replace_report_log = []
            stock_report_log = []
            nse_symbol_change_list = NSEHelper().get_symbol_change_list()
            if nse_symbol_change_list:
                replace_report_log = replace_import_symbol(nse_symbol_change_list)
            nse_stock_list = NSEHelper().get_stock_list()
            if nse_stock_list:
                stock_report_log = save_import_stock(nse_stock_list)
            response_object = {
                'status': 'success',
                'message': 'Stocks successfully imported from NSE',
                'data': {
                    'log': replace_report_log + stock_report_log
                }
            }
            return response_object, 200
        except Exception as e:
            return ErrorSchema.get_response('InternalServerError')

            
class ImportHistoryStockReport(Resource):
    @admin_token_required
    def get(self):
        """Import stock history data from nse/bse and store into database"""
        status = None
        stock_list = get_all_stock()
        NSEHelperObj = NSEHelper()
        for stock in stock_list:
            if stock.id < 0:
                print(stock.symbol+" ====> Completed")
                continue
            print(stock.symbol+' ====> '+str(stock.id))
            report_data = NSEHelperObj.get_history_report(stock.symbol)
            if report_data:
                status = save_history_report(data=report_data, stock_id=stock.id, timeframe='1D')
            if not status:
                break
        if status:
            response_object = {
                'status': 'success',
                'message': 'Stock report successfully imported from NSE/BSE'
            }
            return response_object, 200
        else:
            return ErrorSchema.get_response('InternalServerError')

class ImportDailyStockReport(Resource):
    @admin_token_required
    def get(self):
        """Import stock daily data and store into database"""
        daily_report = NSEHelper().get_daily_report()
        if daily_report:
            return save_daily_report(data=daily_report, timeframe='1D')
        else:
            return ErrorSchema.get_response('InternalServerError')