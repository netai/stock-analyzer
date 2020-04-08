from flask import request
from flask_restful import Resource, reqparse, marshal_with
from ..helpers.auth_helper import Auth
from ..util.dto import AuthDto

class UserLogin(Resource):
    """
        User Login Resource
    """
    def post(self):
        # get the post data
        auth_request = AuthDto.parser.parse_args()
        return Auth.login_user(data=auth_request)

class Logout(Resource):
    """
    User Logout Resource
    """
    def post(self):
        # get auth token
        auth_parser = AuthDto.parser.parse_args()
        auth_header = auth_parser.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)