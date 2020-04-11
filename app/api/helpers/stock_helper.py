from datetime import datetime
from sqlalchemy import func
from app import db
from ..models.stock import Stock
from ..models.stock_day_report import StockDayReport
from ..models.user import User

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
    stock_detail = db.session.query(Stock,StockDayReport).join(StockDayReport, Stock.id==StockDayReport.stock_id)\
        .filter(Stock.symbol==symbol).filter(StockDayReport.series==Stock.series).filter(StockDayReport.exchange_name=='NSE').order_by(StockDayReport.date.desc()).first()
    return stock_detail

def get_stock_data_limit(symbol, limit=1):
    stock_data = db.session.query(Stock,StockDayReport).join(StockDayReport, Stock.id==StockDayReport.stock_id)\
        .filter(Stock.symbol==symbol).filter(StockDayReport.series==Stock.series).filter(StockDayReport.exchange_name=='NSE').order_by(StockDayReport.date.desc()).limit(limit)
    return stock_data

def save_changes(data):
    db.session.add(data)
    db.session.commit()