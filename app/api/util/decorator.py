from functools import wraps
from flask import request
from ..helpers.auth_helper import Auth

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        user_data = data.get('data')
        if not user_data:
            return data, status
        return f(*args, **kwargs)
    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        user_data = data.get('data')
        if not user_data:
            return data, status
        admin = user_data.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401
        return f(*args, **kwargs)
    return decorated
