from datetime import datetime
import uuid
from app import db
from app.models import Stock, StockReport
from ..schema.error_schema import ErrorSchema

def save_import_stock(csv_data):
    """Save stock list from json"""
    try:
        report_log = []
        for row in csv_data:
            stock = Stock.query.filter_by(symbol=row['symbol']).filter_by(exchange_name=row['exchange_name']).first()
            if not stock:
                print(row['symbol'])
                new_stock = Stock(
                    symbol=row['symbol'],
                    company_name=row['company_name'],
                    series=row['series'],
                    listing_date=row['listing_date'],
                    isin_number=row['isin_number'],
                    face_value=row['face_value'],
                    exchange_name=row['exchange_name'],
                    public_id = str(uuid.uuid4()),
                )
                db.session.add(new_stock)
                report_log.append('{} ({})========== INSERTED'.format(row['company_name'], row['symbol']))
            else:
                stock.company_name = row['company_name']
                stock.series = row['series']
                stock.listing_date = row['listing_date']
                stock.isin_number = row['isin_number']
                stock.face_value = row['face_value']
                stock.exchange_name = row['exchange_name']
                db.session.add(stock)
                report_log.append('{} ({})========== UPDATED'.format(row['company_name'], row['symbol']))
        db.session.commit()
        return report_log
    except Exception as e:
        return None

def replace_import_symbol(csv_data):
    """replace new symbol list from json"""
    try:
        report_log = []
        for row in csv_data:
            stock = Stock.query.filter_by(symbol=row['old_symbol']).filter_by(exchange_name=row['exchange_name']).first()
            if stock:
                report_log.append('{} To {} ({})========== REPLACED'.format(row['old_symbol'], row['new_symbol'], str(row['date'])))
        return report_log
    except Exception as e:
        return None

def save_history_report(data, stock_id, timeframe):
    """Save NSE history stock report to Database"""
    try:
        for row in data:
            if row and row['series']=='EQ':
                stock_report = StockReport.query.filter_by(date=row['date']).\
                    filter_by(stock_id=stock_id).filter_by(series=row['series']).first()
                if not stock_report:
                    print(row['date'])
                    new_stock_report = StockReport(
                        date=row['date'],
                        prev_price=row['prev_price'],
                        open_price=row['open_price'],
                        high_price=row['high_price'],
                        low_price=row['low_price'],
                        last_price=row['last_price'],
                        close_price=row['close_price'],
                        avg_price=row['avg_price'],
                        traded_qty=row['traded_qty'],
                        delivery_qty=row['delivery_qty'],
                        series=row['series'],
                        stock_id=stock_id,
                        trade_timeframe=timeframe
                    )
                    db.session.add(new_stock_report)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return None

def save_daily_report(data, timeframe):
    """Save NSE daily stock report to Database"""
    try:
        report_log = []
        for row in data:
            if row and row['series']=='EQ':
                stock = Stock.query.filter_by(symbol=row['symbol']).first()
                if stock:
                    stock_report = StockReport.query.filter_by(date=row['date']).\
                    filter_by(stock_id=stock.id).filter_by(series=row['series']).first()
                    if not stock_report:
                        print(row['symbol'])
                        report_log.append('{} ({})========== INSERTED'.format(row['symbol'], row['date']))
                        new_stock_report = StockReport(
                            date=row['date'],
                            prev_price=row['prev_price'],
                            open_price=row['open_price'],
                            high_price=row['high_price'],
                            low_price=row['low_price'],
                            last_price=row['last_price'],
                            close_price=row['close_price'],
                            avg_price=row['avg_price'],
                            traded_qty=row['traded_qty'],
                            delivery_qty=row['delivery_qty'],
                            series=row['series'],
                            stock_id=stock.id,
                            trade_timeframe=timeframe
                        )
                        db.session.add(new_stock_report)
                    else:
                        report_log.append('{} ({})========== EXISTS'.format(row['symbol'], row['date']))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Stock report successfully imported from NSE',
            'data': {
                'log': report_log
            }
        }
        return response_object, 200
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError')