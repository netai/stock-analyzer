from .. import db

class Fund(db.Model):
    """Fund model for storing fund retated details"""
    __tablename__ = "fund"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Fund 'id: {}, amount: {}'>".format(self.id,self.amount)