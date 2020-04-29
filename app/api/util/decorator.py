from functools import wraps
from flask import request, g
from ..helpers.auth_helper import AuthHelper
from ..schema import ErrorSchema

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_logged_in_user(request)
        user_data = data.get('data')
        if not user_data:
            return data, status
        else:
            g.user = user_data
        return f(*args, **kwargs)
    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_logged_in_user(request)
        user_data = data.get('data')
        if not user_data:
            return data, status
        admin = user_data.get('admin')
        if not admin:
            return ErrorSchema.get_response('InvalidAdminTokenError')
        else:
            g.user = user_data
        return f(*args, **kwargs)
    return decorated
