from flask_restful import Api, Resource, url_for
from flask import Blueprint

from .api.resources.user_resource import UserList, User
from .api.resources.auth_resource import UserLogin, Logout
from .api.resources.import_resource import ImportStock, ImportHistoryStockReport
from .api.resources.stock_resource import StockList

blueprint = Blueprint('api', __name__)

api = Api(blueprint)

"""User related route"""
api.add_resource(User, '/user/<public_id>')
api.add_resource(UserList, '/user')
api.add_resource(UserLogin, '/login')
api.add_resource(Logout, '/logout')

"""Stock related route"""
api.add_resource(StockList, '/stock')

"""Data import related route"""
api.add_resource(ImportStock, '/import/stock')
api.add_resource(ImportHistoryStockReport, '/import/history/day')