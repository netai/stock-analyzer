from flask import g
from app import db
from ..models.order import Order
from ..schema import ErrorSchema
from ..models.stock import Stock
from ..models.stock_report import StockReport
from ..helpers.holding_helper import save_holding
import datetime

def save_order(data):
    try:
        user_id = g.user['id']
        new_order = Order(
            user_id=user_id,
            order_type=data['order_type'],
            is_sell=data['is_sell'],
            price=data['price'],
            qty=data['qty'],
            sl_price=data['sl_price'],
            stock_id=data['stock_id']
        )
        save_changes(new_order)
        response_object = {
            'status': 'success',
            'message': 'Order submitted successfully.'
        }
        return response_object, 200
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_order_all(status=None):
    """return order list"""
    try:
        user_id = g.user['id']
        last_tardes = db.session.query(StockReport.stock_id, StockReport.last_price, db.func.max(StockReport.date)
                                       .label('last_trade_date')).group_by(StockReport.stock_id).subquery()
        order_detail = db.session.query(Order, Stock, last_tardes).join(Stock, Stock.id == Order.stock_id)\
            .join(last_tardes, Order.stock_id == last_tardes.c.stock_id).filter(Order.user_id == user_id).order_by(Order.date.desc())
        if status == 'executed':
            order_detail = order_detail.filter(Order.status.in_(('completed', 'cancelled'))).filter(
                db.func.DATE(Order.executed_date) == datetime.date.today())
        elif status == 'pending':
            order_detail = order_detail.filter(Order.status == status)
        return order_detail
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_a_order(watchlist_no):
    """return single order detail"""
    try:
        pass
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def delete_stock_order(id):
    try:
        user_id = g.user['id']
        order = Order.query.filter_by(id=id).filter_by(user_id=user_id).first()
        if order:
            order.executed_date = datetime.datetime.utcnow()
            order.status = 'cancelled'
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Order cancelled successfully.'
            }
            return response_object, 200
        else:
            return ErrorSchema.get_response('OrderNotExistError')
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_order_json(data):
    order_json = []
    for row in data:
        order_json.append({
            'id': row.Order.id,
            'date': row.Order.date.strftime("%d-%b-%Y %H:%M:%S"),
            'executed_date': row.Order.executed_date.strftime("%d-%b-%Y %H:%M:%S") if row.Order.executed_date else '',
            'order_type': row.Order.order_type,
            'is_sell': row.Order.is_sell,
            'price': row.Order.price,
            'qty': row.Order.qty,
            'sl_price': row.Order.sl_price,
            'status': row.Order.status,
            'stock': {
                'symbol': row.Stock.symbol,
                'exchange_name': row.Stock.exchange_name,
                'last_price': row.last_price,
            }
        })

    return order_json

# Dummy order execution section start here

def get_order_stock_report(order):
    user_id = g.user['id']
    stock_report = StockReport.query.filter(StockReport.low_price <= order.Order.price).filter(StockReport.high_price >= order.Order.price)\
        .filter(StockReport.date >=  db.func.DATE(order.Order.date)).filter(StockReport.stock_id == order.Order.stock_id).order_by(StockReport.date.asc()).first()
    return stock_report

def execute_order():
    try:
        user_id = g.user['id']
        open_order_detail = get_order_all('pending')
        for row in open_order_detail:
            matching_stock_report = get_order_stock_report(row)
            if matching_stock_report:
                order = Order.query.filter_by(
                    id=row.Order.id).filter_by(user_id=user_id).first()
                order.executed_date = matching_stock_report.date
                order.status = 'completed'
                save_holding({
                    'stock_id': row.Order.stock_id,
                    'qty': row.Order.qty,
                    'is_sell': row.Order.is_sell,
                    'price': row.Order.price
                })

                if row.Order.sl_price > 0:
                    save_order({
                        'date': matching_stock_report.date,
                        'order_type': 'market',
                        'is_sell': not row.Order.is_sell,
                        'price': row.Order.sl_price,
                        'qty': row.Order.qty,
                        'sl_price': 0,
                        'stock_id': row.Order.stock_id
                    })
            db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Order executed successfully.'
        }
        return response_object, 200

    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

# Dummy order execution end here

def save_changes(data):
    db.session.add(data)
    db.session.commit()
