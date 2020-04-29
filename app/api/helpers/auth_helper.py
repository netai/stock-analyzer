from ..models.user import User
from ..schema import ErrorSchema
from flask import jsonify

class AuthHelper:
    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'data': {
                            'token': auth_token.decode(),
                            'user': {
                                'name': user.name,
                                'email': user.email,
                                'mobile': user.mobile,
                                'admin': user.admin,
                                'public_id': user.public_id,
                            }
                        }
                    }
                    return response_object, 200
            else:
                return ErrorSchema.get_response('UnauthorizedError')
        except Exception as e:
            return ErrorSchema.get_response('InternalServerError', e)

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
        else:
            return ErrorSchema.get_response('InvalidAuthTokenError')

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, int):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'id': user.id,
                        'name': user.name,
                        'mobile': user.mobile,
                        'email': user.email,
                        'admin': user.admin
                    }
                }
                return response_object, 200
            return resp
        else:
            return ErrorSchema.get_response('InvalidAuthTokenError')
