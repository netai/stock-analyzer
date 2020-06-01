from datetime import datetime
from app import db
from app.models import Stock, StockReport
from ..schema import ErrorSchema


def get_top_delivery(delivery_limit):
    delivery_query = db.session.query(StockReport.stock_id, StockReport.prev_price, StockReport.last_price,\
        ((StockReport.delivery_qty*100.0)/StockReport.traded_qty).label('delivery_per'), db.func.max(StockReport.date)\
            .label('last_trade_date')).group_by(StockReport.stock_id).subquery()
    delivery_detail = db.session.query(Stock, delivery_query).join(delivery_query, Stock.id == delivery_query.c.stock_id)\
        .filter(Stock.series == 'EQ').order_by(delivery_query.c.delivery_per.desc()).limit(delivery_limit).all()
    
    return delivery_detail

def get_top_volumn(volumn_limit):
    volumn_query = db.session.query(StockReport.stock_id, StockReport.prev_price, StockReport.last_price, StockReport.traded_qty,\
        db.func.max(StockReport.date).label('last_trade_date')).group_by(StockReport.stock_id).subquery()
    volumn_detail = db.session.query(Stock, volumn_query).join(volumn_query, Stock.id == volumn_query.c.stock_id)\
        .filter(Stock.series == 'EQ').order_by(volumn_query.c.traded_qty.desc()).limit(volumn_limit).all()
    
    return volumn_detail


def get_top_gainer(gainer_limit):
    gainer_query = db.session.query(StockReport.stock_id, StockReport.prev_price, StockReport.last_price,\
        (((StockReport.prev_price-StockReport.last_price)*100)/StockReport.prev_price).label('change_per'),\
            db.func.max(StockReport.date).label('last_trade_date')).group_by(StockReport.stock_id).subquery()
    gainer_detail = db.session.query(Stock, gainer_query).join(gainer_query, Stock.id == gainer_query.c.stock_id)\
        .filter(Stock.series == 'EQ').order_by(gainer_query.c.change_per.asc()).limit(gainer_limit).all()
    
    return gainer_detail


def get_top_loser(loser_limit):
    loser_query = db.session.query(StockReport.stock_id, StockReport.prev_price, StockReport.last_price,\
        (((StockReport.prev_price-StockReport.last_price)*100)/StockReport.prev_price).label('change_per'),\
            db.func.max(StockReport.date).label('last_trade_date')).group_by(StockReport.stock_id).subquery()
    loser_detail = db.session.query(Stock, loser_query).join(loser_query, Stock.id == loser_query.c.stock_id)\
        .filter(Stock.series == 'EQ').order_by(loser_query.c.change_per.desc()).limit(loser_limit).all()
    
    return loser_detail

