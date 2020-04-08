from datetime import datetime
from ..models.stock import Stock
from ..models.user import User
from .. import db

def save_new_stock(data):
    stock = Stock.query.filter_by(symbol=data['symbol']).first()
    if not stock:
        try:
            new_stock = Stock(
                symbol=data['symbol'],
                company_name=data['company_name'],
                series=data['series'],
                listing_date=datetime.strptime(data['listing_date'], "%d-%b-%Y"),
                isin_number=data['isin_number'],
                face_value=data['face_value'],
                company_detail=data['company_detail']
            )
            save_changes(new_stock)
            response_object = {
                'status': 'success',
                'message': 'Successfully added.'
            }
            return response_object, 201
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 500
    else:
        response_object = {
            'status': 'fail',
            'message': 'Stock already exists.',
        }
        return response_object, 409

def get_all_stock():
    return Stock.query.all()

def get_a_stock(symbol):
    return Stock.query.filter_by(symbol=symbol).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()