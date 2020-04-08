import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ExternalCSV:
    """NSE service url list"""
    NSE_STOCK_LIST = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    NSE_HISTORY_STOCK_REPORT = {
        'STEP1': "https://www1.nseindia.com/marketinfo/sym_map/symbolCount.jsp?symbol={symbol}",
        'STEP2': "https://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol={symbol}&segmentLink=3&symbolCount={symbolCount}&series=ALL&dateRange=12month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE"
    }
    NSE_DAILY_STOCK_REPORT = "https://www1.nseindia.com/products/content/sec_bhavdata_full.csv"