import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ExternalURL:
    """NSE service url list"""
    NSE = {
        'STOCK_LIST' : "https://archives.nseindia.com/content/equities/EQUITY_L.csv",
        'SYMBOL_COUNT' : "https://www1.nseindia.com/marketinfo/sym_map/symbolCount.jsp?symbol={symbol}",
        'HISTORY_REPORT' : "https://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol={symbol}&segmentLink=3&symbolCount={symbolCount}&series=EQ&dateRange=12month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE",
        'DAILY_REPORT' : "https://www1.nseindia.com/products/content/sec_bhavdata_full.csv",
        'SYMBOL_CHANGE': "https://archives.nseindia.com/content/equities/symbolchange.csv"
    }

    BSE = {
        'STOCK_LIST': "https://www.bseindia.com/corporates/List_Scrips.aspx"
    }