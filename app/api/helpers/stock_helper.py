from datetime import datetime
from ..models.stock import Stock
from ..models.stock_day_report import StockDayReport
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
    stock = Stock.query.filter_by(symbol=symbol).first()
    last_day_report = StockDayReport.query.filter_by(stock_id=stock.id).filter_by(exchange_name='NSE').order_by(StockDayReport.date.desc()).first()
    return_data = {
        'id': stock.id,
        'symbol': stock.symbol,
        'company_name': stock.company_name,
        'series': stock.series,
        'listing_date': str(stock.listing_date),
        'isin_number': stock.isin_number,
        'face_value': stock.face_value,
        'company_detail': stock.company_detail,
        'comapany_website': stock.company_website,
        'trade_detail': {
            'nse': {
                'date': str(last_day_report.date),
                'open_price': last_day_report.open_price,
                'high_price': last_day_report.high_price,
                'low_price': last_day_report.low_price,
                'last_price': last_day_report.last_price,
                'close_price': last_day_report.close_price,
                'avg_price': last_day_report.avg_price,
                'traded_qty': last_day_report.traded_qty,
                'dlvry_qty': last_day_report.delivery_qty,
                'dlvry_per': '',
                'avg_dlvry_per': '',
            }
        }
    }
    return return_data

def save_changes(data):
    db.session.add(data)
    db.session.commit()