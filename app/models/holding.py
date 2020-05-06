from .. import db

class Holding(db.Model):
    """Holding model for storing order retated details"""
    __tablename__ = "holding"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qty = db.Column(db.Integer, nullable=False)
    avg_price = db.Column(db.Float, nullable=False)
    inv_amount = db.Column(db.Float, nullable=False)
    is_sell = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.String(20), nullable=False, default='hold')
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Holding 'id: {}, status: {}'>".format(self.id,self.status)