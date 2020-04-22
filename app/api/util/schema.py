from flask_restful import fields

class UserSchema():
    user_list = {
        'name': fields.String,
        'mobile': fields.String,
        'email': fields.String,
        'admin': fields.String,
        'public_id': fields.String,
        'exchange_name': fields.String
    }

class StockSchema():
    stock_list = {
        'id': fields.Integer,
        'symbol': fields.String,
        'company_name': fields.String,
        'series': fields.String,
        'listing_date': fields.String,
        'isin_number': fields.String,
        'face_value': fields.Integer,
        'company_detail': fields.String,
        'comapany_website': fields.String,
        'exchange_name': fields.String
    }