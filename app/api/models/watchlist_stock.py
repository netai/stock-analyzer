from app import db

class WatchlistStock(db.Model):
    """watchlist stock model for storing watchlist stock"""
    __tablename__ = "watchlist_stock"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    watchlist_no = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    note = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<Watchlist '{}'>".format(self.watchlist_no)