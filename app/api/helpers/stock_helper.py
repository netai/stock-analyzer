from datetime import datetime
from sqlalchemy import func
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
    stock_detail = db.session.query(Stock,StockDayReport,func.avg(StockDayReport.traded_qty).label('traded_qty_avg'),func.avg(StockDayReport.delivery_qty).label('delivery_qty_avg')).join(StockDayReport, Stock.id==StockDayReport.stock_id)\
        .filter(Stock.symbol==symbol).filter(StockDayReport.exchange_name=='NSE').order_by(StockDayReport.date.desc()).first()
    print(str(stock_detail))
    return_data = {
        'id': stock_detail.Stock.id,
        'symbol': stock_detail.Stock.symbol,
        'company_name': stock_detail.Stock.company_name,
        'series': stock_detail.Stock.series,
        'listing_date': str(stock_detail.Stock.listing_date),
        'isin_number': stock_detail.Stock.isin_number,
        'face_value': stock_detail.Stock.face_value,
        'company_detail': stock_detail.Stock.company_detail,
        'comapany_website': stock_detail.Stock.company_website,
        'trade_detail': {
            'nse': {
                'date': str(stock_detail.StockDayReport.date),
                'open_price': stock_detail.StockDayReport.open_price,
                'high_price': stock_detail.StockDayReport.high_price,
                'low_price': stock_detail.StockDayReport.low_price,
                'last_price': stock_detail.StockDayReport.last_price,
                'close_price': stock_detail.StockDayReport.close_price,
                'avg_price': stock_detail.StockDayReport.avg_price,
                'traded_qty': stock_detail.StockDayReport.traded_qty,
                'dlvry_qty': stock_detail.StockDayReport.delivery_qty,
                'dlvry_per': round((stock_detail.StockDayReport.delivery_qty/stock_detail.StockDayReport.traded_qty)*100, 2),
                'avg_dlvry_per': round((stock_detail.delivery_qty_avg/stock_detail.traded_qty_avg)*100, 2),
            }
        }
    }
    return return_data

def save_changes(data):
    db.session.add(data)
    db.session.commit()