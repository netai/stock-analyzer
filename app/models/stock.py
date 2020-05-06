from .. import db

class Stock(db.Model):
    """Stock model for storing stock retated details"""
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(20), nullable=False, unique=True)
    company_name = db.Column(db.String(255), nullable=False)
    series = db.Column(db.String(3), nullable=False)
    listing_date = db.Column(db.Date, nullable=False)
    isin_number = db.Column(db.String(20), nullable=False)
    face_value = db.Column(db.Integer, nullable=False)
    company_detail = db.Column(db.Text, nullable=True)
    company_website = db.Column(db.String(255), nullable=True)
    exchange_name = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return "<Stock '{}'>".format(self.symbol)