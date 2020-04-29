from flask_restful import Resource
from ..util.decorator import token_required
from ..schema import ErrorSchema
from ..helpers.order_helper import get_order_all, save_order, get_order_json, delete_stock_order
from ..util.dto import OrderDto

class OrderList(Resource):
    @token_required
    def get(self):
        """List all added order detail"""
        try:
            open_order_detail = get_order_json(get_order_all('pending'))
            executed_order_detail = get_order_json(get_order_all('executed'))
            response_object = {
                'status': 'success',
                'data': {
                    'order': {
                        'open_order': open_order_detail,
                        'executed_order': executed_order_detail
                    }
                }
            }
            return response_object, 200
        except Exception as e:
            return ErrorSchema.get_response('InternalServerError', e)
    
    @token_required
    def post(self):
        """add a new order"""
        order_request = OrderDto.parser.parse_args()
        return save_order(data=order_request)

    @token_required
    def delete(self, id):
        """delete order"""
        delete_stock_order(id=id)
        response_object = {
            'status': 'success',
            'message': 'Order cancelled successfully.'
        }
        return response_object, 200
