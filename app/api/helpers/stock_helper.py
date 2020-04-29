from datetime import datetime
from app import db
from ..models.stock import Stock
from ..models.stock_report import StockReport
from ..schema import ErrorSchema

def save_new_stock(data):
    try:
        stock = Stock.query.filter_by(symbol=data['symbol']).filter_by(
            exchange_name=data['exchange_name']).first()
        if not stock:
            new_stock = Stock(
                symbol=data['symbol'],
                company_name=data['company_name'],
                series=data['series'],
                listing_date=datetime.strptime(data['listing_date'], "%d-%b-%Y"),
                isin_number=data['isin_number'],
                face_value=data['face_value'],
                company_detail=data['company_detail'],
                exchange_name=data['exchange_name']
            )
            save_changes(new_stock)
            response_object = {
                'status': 'success',
                'message': 'Successfully added.'
            }
            return response_object, 201
        else:
            return ErrorSchema.get_response('StockExistError')
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_all_stock():
    try:
        return Stock.query.all()
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_a_stock(id):
    try:
        stock_detail = db.session.query(Stock, StockReport).join(StockReport, Stock.id == StockReport.stock_id)\
            .filter(Stock.id == id).filter(StockReport.series == Stock.series).order_by(StockReport.date.desc()).first()
        return stock_detail
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def save_changes(data):
    db.session.add(data)
    db.session.commit()
