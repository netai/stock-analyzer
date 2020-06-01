from flask_restful import Resource
from ..util.decorator import token_required
from ..util.dto import ActivityDto
from ..schema import ErrorSchema
from ..helpers.activity_helper import get_top_delivery, get_top_volumn, get_top_gainer, get_top_loser

class ActivityIndex(Resource):
    @token_required
    def get(self):
        """activity list"""
        activity_request = ActivityDto.parser.parse_args()
        try:
            delivery_list = get_top_delivery(activity_request['delivery_limit'])
            volumn_list = get_top_volumn(activity_request['volumn_limit'])
            gainer_list = get_top_gainer(activity_request['gainer_limit'])
            loser_list = get_top_loser(activity_request['loser_limit'])
            top_delivery = []
            top_volumn = []
            top_gainer = []
            top_loser = []

            #create json for top delivery
            for row in delivery_list:
                top_delivery.append({
                    'symbol': row.Stock.symbol,
                    'exchange_name': row.Stock.exchange_name,
                    'prev_price': row.prev_price,
                    'last_price': row.last_price,
                    'change_per': round((abs(row.prev_price-row.last_price)/row.prev_price)*100, 2),
                    'delivery_per': round(row.delivery_per, 2)
                })

            #create json for top volumn
            for row in volumn_list:
                top_volumn.append({
                    'symbol': row.Stock.symbol,
                    'exchange_name': row.Stock.exchange_name,
                    'prev_price': row.prev_price,
                    'last_price': row.last_price,
                    'change_per': round((abs(row.prev_price-row.last_price)/row.prev_price)*100, 2),
                    'traded_qty': row.traded_qty
                })

            #create json for top gainer
            for row in gainer_list:
                top_gainer.append({
                    'symbol': row.Stock.symbol,
                    'exchange_name': row.Stock.exchange_name,
                    'prev_price': row.prev_price,
                    'last_price': row.last_price,
                    'change_per': round(abs(row.change_per), 2)
                })
            
            #create json for top loser
            for row in loser_list:
                top_loser.append({
                    'symbol': row.Stock.symbol,
                    'exchange_name': row.Stock.exchange_name,
                    'prev_price': row.prev_price,
                    'last_price': row.last_price,
                    'change_per': round(abs(row.change_per), 2)
                })

            respoonse_object = {
                'status': 'success',
                'data': {
                    'top_delivery': top_delivery,
                    'top_volumn': top_volumn,
                    'top_gainer': top_gainer,
                    'top_loser': top_loser
                }
            }
            return respoonse_object, 200
        except Exception as e:
            return ErrorSchema.get_response('InternalServerError', e)