from datetime import datetime
from ..models.stock import Stock
from ..models.stock_day_report import StockDayReport
from .. import db

def save_stock_from_nse(csv_data):
    try:
        next(csv_data)
        for row in csv_data:
            stock = Stock.query.filter_by(symbol=row[0]).first()
            if not stock:
                new_stock = Stock(
                    symbol=row[0].strip(),
                    company_name=row[1].strip(),
                    series=row[2].strip(),
                    listing_date=datetime.strptime(row[3].strip(), "%d-%b-%Y"),
                    isin_number=row[6].strip(),
                    face_value=row[7].strip()
                )
                db.session.add(new_stock)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def save_stock_report_from_nse(csv_data, stock_id):
    try:
        next(csv_data)
        for row in csv_data:
            if row:
                date = datetime.strptime(row[2].strip(), "%d-%b-%Y").date()
                stock_report = StockDayReport.query.filter_by(date=date).\
                    filter_by(stock_id=stock_id).first()
                if not stock_report:
                    print(date)
                    new_stock_report = StockDayReport(
                        date=datetime.strptime(row[2].strip(), "%d-%b-%Y"),
                        open_price=row[4].strip(),
                        high_price=row[5].strip(),
                        low_price=row[6].strip(),
                        last_price=row[7].strip(),
                        close_price=row[8].strip(),
                        avg_price=row[9].strip(),
                        traded_qty=row[10].strip(),
                        delivery_qty=row[13].strip(),
                        exchange_name='NSE',
                        stock_id=stock_id
                    )
                    db.session.add(new_stock_report)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False