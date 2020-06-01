from flask_restful import Resource, reqparse, fields

class UserDto:
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('mobile', type=str, help='This field cannot be left blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

class AuthDto:
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

class StockDto:
    parser = reqparse.RequestParser()
    parser.add_argument('symbol', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('company_name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('series', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('listing_date', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('isin_number', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('face_value', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('company_detail', type=str, help='Company Detail')
    parser.add_argument('company_website', type=str, help='Company Website')

class StockReportDto:
    parser = reqparse.RequestParser()
    parser.add_argument('from_date', type=str, required=True, help='This field cannot be left blank', location='args')
    parser.add_argument('to_date', type=str, required=True, help='This field cannot be left blank', location='args')

class WatchlistDto:
    parser = reqparse.RequestParser()
    parser.add_argument('stock_id', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('watchlist_no', type=int, required=True, help='This field cannot be left blank')

class OrderDto:
    parser = reqparse.RequestParser()
    parser.add_argument('is_sell', type=bool, required=True, help='This field cannot be left blank')
    parser.add_argument('order_type', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('qty', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('sl_price', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('stock_id', type=int, required=True, help='This field cannot be left blank')

class ActivityDto:
    parser = reqparse.RequestParser()
    parser.add_argument('delivery_limit', type=int, required=True, help='This field cannot be left blank', location='args')
    parser.add_argument('volumn_limit', type=int, required=True, help='This field cannot be left blank', location='args')
    parser.add_argument('gainer_limit', type=int, required=True, help='This field cannot be left blank', location='args')
    parser.add_argument('loser_limit', type=int, required=True, help='This field cannot be left blank', location='args')