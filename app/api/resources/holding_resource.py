from flask_restful import Resource
from ..util.decorator import token_required
from ..schema import ErrorSchema
from ..helpers.holding_helper import get_holding_all

class HoldingList(Resource):
    @token_required
    def get(self):
        """List all added holding detail"""
        try:
            holding_detail = get_holding_all()
            holding_json = []
            for row in holding_detail:
                if row.Holding.is_sell:
                    cur_value = round(row.Holding.inv_amount + ((row.Holding.avg_price - row.last_price) * row.Holding.qty), 2)
                else:
                    cur_value = round(row.Holding.inv_amount + ((row.last_price - row.Holding.avg_price) * row.Holding.qty), 2)
                holding_json.append({
                    'id': row.Holding.id,
                    'qty': row.Holding.qty,
                    'avg_price': row.Holding.avg_price,
                    'inv_amount': row.Holding.inv_amount,
                    'cur_value': abs(cur_value),
                    'pl_value': "{0:+}".format(cur_value - row.Holding.inv_amount ),
                    'net_change': "{0:+}".format(round(((cur_value - row.Holding.inv_amount)/row.Holding.inv_amount)* 100, 2)),
                    'is_sell': row.Holding.is_sell,
                    'stock': {
                        'id': row.Stock.id,
                        'symbol': row.Stock.symbol,
                        'exchange_name': row.Stock.exchange_name,
                        'last_price': row.last_price,
                        'prev_price': row.prev_price,
                        'per_change': round((abs(row.prev_price-row.last_price)/row.prev_price)*100, 2)
                    }
                })
            response_object = {
                'status': 'success',
                'data': {
                    'holding': holding_json
                }
            }
            return response_object, 200
        except Exception as e:
            return ErrorSchema.get_response('InternalServerError', e)
