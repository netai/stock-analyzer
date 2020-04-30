from .resources import UserList, User, Login, Logout, ImportStock, ImportHistoryStockReport,\
    ImportDailyStockReport, StockList, Stock, StockIndicator, StockListIndicator, Watchlist,\
        OrderList, OrderExecute, HoldingList

def api_routes(api):
    """Auth related route"""
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')

    """User related route"""
    api.add_resource(User, '/user/<public_id>')
    api.add_resource(UserList, '/user')

    """Stock related route"""
    api.add_resource(StockList, '/stock')
    api.add_resource(Stock, '/stock/<id>')


    """Data import related route"""
    api.add_resource(ImportStock, '/import/stock')
    api.add_resource(ImportHistoryStockReport, '/import/history/day')
    api.add_resource(ImportDailyStockReport, '/import/report/day')

    """Stock analysis related route"""
    api.add_resource(StockIndicator, '/analyzer/indicator/<symbol>')
    api.add_resource(StockListIndicator, '/analyzer/indicator')

    """watchlist related route"""
    api.add_resource(
        Watchlist,
        '/watchlist',
        '/watchlist/<int:watchlist_no>/stock/<int:stock_id>'
        )

    """Order related route"""
    api.add_resource(
        OrderList,
        '/order',
        '/order/<int:id>'
        )

    """manualy Execute order"""
    api.add_resource(OrderExecute, '/order/execute')

    """holding related route"""
    api.add_resource(HoldingList, '/holding')