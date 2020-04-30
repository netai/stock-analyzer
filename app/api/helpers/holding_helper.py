from flask import g
from app import db
from ..models.holding import Holding
from ..models.stock_report import StockReport
from ..models.stock import Stock
from ..schema import ErrorSchema

def save_holding(data):
    user_id = g.user['id']
    holding = Holding.query.filter_by(user_id=user_id).filter_by(stock_id=data['stock_id']).first()
    if holding:
        if data['is_sell'] == holding.is_sell:
            qty = holding.qty + data['qty']
            inv_amount = holding.inv_amount + (data['price'] * data['qty'])
            avg_price = round(inv_amount/qty, 2)
        else:
            qty = holding.qty - data['qty']
            inv_amount = holding.inv_amount - (data['price'] * data['qty'])
            # insert (data['price'] * data['qty']) amount to fund
            avg_price = round(inv_amount/qty, 2)
        if qty <= 0:
            qty = abs(qty)
            Holding.query.filter_by(user_id=user_id).filter_by(stock_id=data['stock_id']).delete()
            insert_holding({
                'qty': qty,
                'inv_amount': (data['price'] * qty),
                'is_sell': data['is_sell'],
                'stock_id': data['stock_id'],
                'user_id': user_id
            })
        else:
            holding.qty = qty
            holding.inv_amount = inv_amount
            holding.avg_price = avg_price

        db.session.commit()
        return True
    else:
        return insert_holding({
            'qty': data['qty'],
            'inv_amount': (data['price'] * data['qty']),
            'is_sell': data['is_sell'],
            'stock_id': data['stock_id'],
            'user_id': user_id
        })

def insert_holding(data):
    if data['qty'] > 0:
        new_holding = Holding(
            qty=data['qty'],
            avg_price=round(data['inv_amount']/data['qty'], 2),
            inv_amount=data['inv_amount'],
            is_sell=data['is_sell'],
            stock_id=data['stock_id'],
            user_id=data['user_id'],
        )
        save_changes(new_holding)
        return True
    else:
        return None

def get_holding_all(status=None):
    """return holding list"""
    try:
        user_id = g.user['id']
        last_tardes = db.session.query(StockReport.stock_id, StockReport.prev_price, StockReport.last_price, db.func.max(StockReport.date)
                                       .label('last_trade_date')).group_by(StockReport.stock_id).subquery()
        holding_detail = db.session.query(Holding, Stock, last_tardes).join(Stock, Stock.id == Holding.stock_id)\
            .join(last_tardes, Holding.stock_id == last_tardes.c.stock_id).filter(Holding.user_id == user_id)
        return holding_detail
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def save_changes(data):
    db.session.add(data)
    db.session.commit()
