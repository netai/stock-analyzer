from flask_restful import Resource, marshal, marshal_with
from ..util.decorator import admin_token_required, token_required
from ..helpers.watchlist_helper import get_watchlist_all,save_stock_watchlist,get_a_watchlist,delete_stock_watchlist
from ..util.dto import WatchlistDto

class Watchlist(Resource):
    @token_required
    def get(self):
        """List all added watchlist detail"""
        watchlist_detail = get_watchlist_all()
        print(watchlist_detail)
        watchlist_json = []
        watchlist_no = None
        lastIndx = -1
        for row in watchlist_detail:
            print(row)
            if watchlist_no != row.WatchlistStock.watchlist_no:
                lastIndx += 1
                watchlist_json.insert(lastIndx, {
                    'watchlist_no': row.WatchlistStock.watchlist_no,
                    'stocks': []
                })
                watchlist_no = row.WatchlistStock.watchlist_no

            change_per = round((abs(row.prev_price-row.last_price)/row.prev_price)*100, 2)
            watchlist_json[lastIndx]['stocks'].append({
                'id': row.Stock.id,
                'symbol': row.Stock.symbol,
                'traded_date': str(row.last_trade_date),
                'company_name': row.Stock.company_name,
                'exchange_name': row.Stock.exchange_name,
                'prev_price': row.prev_price,
                'last_price': row.last_price,
                'change_per': change_per,
                'note': row.WatchlistStock.note if row.WatchlistStock.note else ''
            })
        response_object = {
            'status': 'success',
            'data': {
                'watchlist': watchlist_json
            }
        }
        return response_object, 200
    
    @token_required
    def post(self):
        """add a new stock"""
        watchlist_request = WatchlistDto.parser.parse_args()
        save_stock_watchlist(data=watchlist_request)
        watchlist_detail = get_a_watchlist(watchlist_request.watchlist_no)
        watchlist_json = {
            'watchlist_no': watchlist_request.watchlist_no,
            'stocks': []
        }
        for row in watchlist_detail:
            change_per = round((abs(row.prev_price-row.last_price)/row.prev_price)*100, 2)
            watchlist_json['stocks'].append({
                'id': row.Stock.id,
                'symbol': row.Stock.symbol,
                'traded_date': str(row.last_trade_date),
                'company_name': row.Stock.company_name,
                'exchange_name': row.Stock.exchange_name,
                'prev_price': row.prev_price,
                'last_price': row.last_price,
                'change_per': change_per,
                'note': row.WatchlistStock.note if row.WatchlistStock.note else ''
            })
        response_object = {
            'status': 'success',
            'data': {
                'watchlist': watchlist_json
            }
        }
        return response_object, 200

    @token_required
    def delete(self, watchlist_no, stock_id):
        """delete stock"""
        delete_stock_watchlist({'watchlist_no': watchlist_no, 'stock_id': stock_id})
        watchlist_detail = get_a_watchlist(watchlist_no)
        watchlist_json = {
            'watchlist_no': watchlist_no,
            'stocks': []
        }
        for row in watchlist_detail:
            change_per = round((abs(row.prev_price-row.last_price)/row.prev_price)*100, 2)
            watchlist_json['stocks'].append({
                'id': row.Stock.id,
                'symbol': row.Stock.symbol,
                'traded_date': str(row.last_trade_date),
                'company_name': row.Stock.company_name,
                'exchange_name': row.Stock.exchange_name,
                'prev_price': row.prev_price,
                'last_price': row.last_price,
                'change_per': change_per,
                'note': row.WatchlistStock.note if row.WatchlistStock.note else ''
            })
        response_object = {
            'status': 'success',
            'data': {
                'watchlist': watchlist_json
            }
        }
        return response_object, 200
