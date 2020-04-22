from flask_restful import Resource, marshal, marshal_with
from ..util.decorator import admin_token_required, token_required
from ..util.dto import UserDto
from ..util.schema import UserSchema
from ..helpers.user_helper import save_new_user, get_all_users, get_a_user

class UserList(Resource):
    @admin_token_required
    def get(self):
        """List all registered users"""
        users_list = get_all_users()
        response_object = {
            'status': 'success',
            'data': {
                'users': marshal(users_list, UserSchema.user_list)
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
        response_object = {
            'status': 'success',
            'data': {
                'user': marshal(user, UserSchema.user_list)
            }
        }
        return response_object, 200
