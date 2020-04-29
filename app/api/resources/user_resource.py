from flask_restful import Resource, marshal
from ..util.decorator import admin_token_required, token_required
from ..util.dto import UserDto
from ..helpers.user_helper import save_new_user, get_all_users, get_a_user
from ..schema import ErrorSchema

class UserList(Resource):
    @admin_token_required
    def get(self):
        """List all registered users"""
        users_list = get_all_users()
        response_object = {
            'status': 'success',
            'data': {
                'users': marshal(users_list, user_list)
            }
        }
        return response_object, 200

    def post(self):
        """Creates a new User """
        user_request = UserDto.parser.parse_args()
        return save_new_user(data=user_request)

class User(Resource):
    @token_required
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if user:
            response_object = {
                'status': 'success',
                'data': {
                    'user': {
                        'name': user.name,
                        'email': user.email,
                        'mobile': user.mobile,
                        'admin': user.admin,
                        'public_id': user.public_id
                    }
                }
            }
            return response_object, 200
        else:
            return ErrorSchema.get_response('UserNotExistError')
