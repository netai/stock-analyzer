import datetime
from .. import db

class Order(db.Model):
    """Order model for storing order retated details"""
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    order_type = db.Column(db.String(10), nullable=False)
    is_sell = db.Column(db.Boolean, nullable=False, default=False)
    price = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    sl_price = db.Column(db.Float, nullable=False, default=0)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executed_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='pending')

    def __repr__(self):
        return "<Order 'id: {}, date: {}, status: {}'>".format(self.id,str(self.date),self.status)