from flask import Blueprint
from .views.live_stock_view import index

stream_blueprint = Blueprint('stream', __name__, url_prefix='/stream')

stream_blueprint.add_url_rule('/live/stock', endpoint='livestock', view_func=index, methods=["GET"])