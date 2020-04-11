from flask import Blueprint
from flask_restful import Api
from .resources.user_resource import UserList, User
from .resources.auth_resource import UserLogin, Logout
from .resources.import_resource import ImportStock, ImportHistoryStockReport, ImportDailyStockReport
from .resources.stock_resource import StockList, Stock
from .resources.analyzer_resource import StockIndicator, StockListIndicator

blueprint = Blueprint('api', __name__, url_prefix="/api")
api = Api(blueprint)

"""User related route"""
api.add_resource(User, '/user/<public_id>')
api.add_resource(UserList, '/user')
api.add_resource(UserLogin, '/login')
api.add_resource(Logout, '/logout')

"""Stock related route"""
api.add_resource(StockList, '/stock')
api.add_resource(Stock, '/stock/<symbol>')


"""Data import related route"""
api.add_resource(ImportStock, '/import/stock')
api.add_resource(ImportHistoryStockReport, '/import/history/day')
api.add_resource(ImportDailyStockReport, '/import/report/day')

"""Stock analysis related route"""
api.add_resource(StockIndicator, '/analyzer/indicator/<symbol>')
api.add_resource(StockListIndicator, '/analyzer/indicator')
