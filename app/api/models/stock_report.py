from app import db

class StockReport(db.Model):
    """Stock Report model for storing stock report retated details"""
    __tablename__ = "stock_report"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    prev_price = db.Column(db.Float, nullable=False)
    open_price = db.Column(db.Float, nullable=False)
    high_price = db.Column(db.Float, nullable=False)
    low_price = db.Column(db.Float, nullable=False)
    last_price = db.Column(db.Float, nullable=True)
    close_price = db.Column(db.Float, nullable=False)
    avg_price = db.Column(db.Float, nullable=True)
    traded_qty = db.Column(db.Integer, nullable=True)
    delivery_qty = db.Column(db.Integer, nullable=True)
    series = db.Column(db.String(3), nullable=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    trade_timeframe = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return "<stock_report '{}'>".format(self.id)