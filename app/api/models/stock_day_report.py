from .. import db

class StockDayReport(db.Model):
    """Stock Report model for storing stock report retated details"""
    __tablename__ = "stock_day_report"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    open_price = db.Column(db.Float, nullable=False)
    high_price = db.Column(db.Float, nullable=False)
    low_price = db.Column(db.Float, nullable=False)
    last_price = db.Column(db.Float, nullable=False)
    close_price = db.Column(db.Float, nullable=False)
    avg_price = db.Column(db.Float, nullable=True)
    traded_qty = db.Column(db.Integer, nullable=True)
    delivery_qty = db.Column(db.Integer, nullable=True)
    exchange_name = db.Column(db.String(4), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))

    def __repr__(self):
        return "<stock_day_report '{}'>".format(self.id)