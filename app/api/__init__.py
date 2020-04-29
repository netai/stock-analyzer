from flask import Blueprint
from flask_restful import Api
from .routes import api_routes

api_blueprint = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_blueprint)
api_routes(api)