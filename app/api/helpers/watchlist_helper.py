from flask import g
from app import db
from ..models.stock import Stock
from ..models.watchlist_stock import WatchlistStock
from ..models.stock_report import StockReport
from ..schema import ErrorSchema

def save_stock_watchlist(data):
    try:
        user_id = g.user['id']
        watchlist = WatchlistStock.query.filter_by(watchlist_no=data['watchlist_no'])\
            .filter_by(user_id=user_id).filter_by(stock_id=data['stock_id']).first()
        if not watchlist:
            new_watchlist = WatchlistStock(
                user_id=user_id,
                watchlist_no=data['watchlist_no'],
                stock_id=data['stock_id'],
            )
            save_changes(new_watchlist)
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_watchlist_all():
    """return watchlist with stock"""
    try:
        user_id = g.user['id']
        last_tardes = db.session.query(StockReport.stock_id, StockReport.series, StockReport.prev_price, StockReport.last_price, db.func.max(StockReport.date)\
            .label('last_trade_date')).group_by(StockReport.stock_id).subquery()
        watchlist_detail = db.session.query(WatchlistStock,Stock,last_tardes).join(Stock, Stock.id==WatchlistStock.stock_id)\
            .join(last_tardes, WatchlistStock.stock_id==last_tardes.c.stock_id).filter(last_tardes.c.series==Stock.series)\
                .filter(WatchlistStock.user_id==user_id).order_by(WatchlistStock.watchlist_no.asc()).order_by(Stock.symbol.asc())
        return watchlist_detail
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def get_a_watchlist(watchlist_no):
    """return single watchlist with stock"""
    try:
        user_id = g.user['id']
        last_tardes = db.session.query(StockReport.stock_id, StockReport.series, StockReport.prev_price, StockReport.last_price, db.func.max(StockReport.date)\
            .label('last_trade_date')).group_by(StockReport.stock_id).subquery()
        watchlist_detail = db.session.query(WatchlistStock,Stock,last_tardes).join(Stock, Stock.id==WatchlistStock.stock_id)\
            .join(last_tardes, WatchlistStock.stock_id==last_tardes.c.stock_id).filter(last_tardes.c.series==Stock.series)\
                .filter(WatchlistStock.watchlist_no==watchlist_no).filter(WatchlistStock.user_id==user_id)\
                    .order_by(WatchlistStock.watchlist_no.asc()).order_by(Stock.symbol.asc())
        return watchlist_detail
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def delete_stock_watchlist(data):
    try:
        user_id = g.user['id']
        watchlist = WatchlistStock.query.filter_by(watchlist_no=data['watchlist_no'])\
            .filter_by(user_id=user_id).filter_by(stock_id=data['stock_id']).delete()
        db.session.commit()
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def save_changes(data):
    db.session.add(data)
    db.session.commit()