from flask import Blueprint
from .views.home_view import index, apiIndex

main_blueprint = Blueprint('main', __name__,
    template_folder='templates',
    static_folder='static', url_prefix='/')

main_blueprint.add_url_rule('', endpoint='index', view_func=index, methods=["GET"])
main_blueprint.add_url_rule('/api', endpoint='apiindex', view_func=apiIndex, methods=["GET"])