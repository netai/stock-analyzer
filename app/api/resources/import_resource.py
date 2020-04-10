from flask_restful import Resource
import csv
import requests
from bs4 import BeautifulSoup
from ..util.decorator import admin_token_required
from ..helpers.import_helper import save_stk_nse, save_stk_rpt_nse, save_dly_stk_rpt_nse
from ..helpers.stock_helper import get_all_stock
from ..constants import ExternalCSV

class ImportStock(Resource):
    @admin_token_required
    def get(self):
        """Import stocks from nse/bse website and store into database"""
        """Start NSE Block"""
        downloaded_response = requests.get(ExternalCSV.NSE_STOCK_LIST)
        csv_reader = csv.reader(downloaded_response.content.decode('utf-8').splitlines(), delimiter=',')
        status = save_stk_nse(csv_reader)
        """End NSE Block"""
        if status:
            respoonse_object = {
                'status': 'success',
                'message': 'Stock list successfully imported from NSE/BSE'
            }
            return respoonse_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return respoonse_object, 500

class ImportHistoryStockReport(Resource):
    @admin_token_required
    def get(self):
        """Import stock history data for 1 year and store into database"""
        """Start NSE Block"""
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Referer': 'https://www1.nseindia.com/products/content/equities/equities/eq_security.htm',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'www1.nseindia.com',
            'Cookie': 'sym1=TCS; sym2=WIPRO; _ga=GA1.2.270553252.1586297590; sym3=WSTCSTPAPR; pointer=3; NSE-TEST-1=1927290890.20480.0000; _gid=GA1.2.1756842089.1586456257; ak_bmsc=A139AF98E935116268EECBB7EB4964DF17CB3F0E95500000AA7B8F5E8465F26D~plmvICUQPUrdgrGHCpkDp4GxHFnJClHmLVA+KeTVdBEaW8eSDZYDf8sDdinTfezHBXJ9K6KT/Gzqq+HE4t6V/WLOpWe7FIcROspez0JVc8HhHuMpbZ1Ug80I1DDCnkF9rG0KuES3uDH+MHtENPZnJsNny3kJRUxVYpQsLj/WAhHbbs9KUvNbMZUs8fNvZ5IGPq3TKiCzruyFk64lkhz8J+O6oJvB5BqMJDmkMq88ahJ+4=; bm_mi=CB1EB2DC0E366F7FFC8A9A8BAAA42DCB~oFa+hnNsrUOZZcivDwg/zmLSC3IqU4FLU/vsdqVmYix0knAF45VZNpw8BKOdIgRjfxEzLvN6aOcPgqi3PAoF4BFyTtgHCvaomog2vlsediI2hGnFtQz+zv/tC9SccQgabQq82+j594t01elud1Bnwne8XydTlhJTxy9uF2fq57+mioHJrVm4IMb2uKRF8pGDansKnyVxFTB1e0fY4o4sGYGspXVhR6B4PHVKhzTOiJUedJ3S06YLhShEyb3LUYiwT7nXSZL6PPKVQ862M1hmW17k2lPJU7KXpuo8/1fLPgk=; RT="z=1&dm=nseindia.com&si=ce6a7f89-dc0d-4870-a97e-07dbe084f7ff&ss=k8t1zkdb&sl=1&tt=7v&bcn=%2F%2F684fc53b.akstat.io%2F&ld=5s4u6"; JSESSIONID=47896D0BBDBE722051458673276E4233.tomcat2; bm_sv=A4586E30B481ADB6D78D1D40CA94F0CC~LcTrwXihd7jPfcKmZhnbgfjbfHoS+uZAdquzEbEmjZ1oxV9Qi1L30wxLIq4LjKFRL5ufDzGDO9+GwJHaMHhgp5/KUZBnUweI3lhKOa/GusXkrhN4qbucvKaqpQF3nD5B9LOYoCxVxJbisW3Z0xNcoJfIXqWD8fspFAa1fylnBsw=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        status = False
        stock_list = get_all_stock()
        for stock in stock_list:
            if stock.id < 0:
                print(stock.symbol+" ====> Completed")
                continue
            print(stock.symbol+' ====> '+str(stock.id))
            symbol_count_response = requests.get(url=ExternalCSV.NSE_HISTORY_STOCK_REPORT['STEP1'].format(symbol=requests.utils.quote(stock.symbol)), headers=headers)
            downloaded_response = requests.get(ExternalCSV.NSE_HISTORY_STOCK_REPORT['STEP2'].format(symbol=requests.utils.quote(stock.symbol),symbolCount=symbol_count_response.text.strip()), headers=headers)
            print(ExternalCSV.NSE_HISTORY_STOCK_REPORT['STEP2'].format(symbol=stock.symbol,symbolCount=symbol_count_response.text.strip()))
            soup = BeautifulSoup(downloaded_response.text, 'html.parser')
            content_obj = soup.find('div', id='csvContentDiv')
            if content_obj:
                csv_content = content_obj.text.split(':')
                csv_reader = csv.reader(csv_content, delimiter=',')
                status = save_stk_rpt_nse(csv_reader, stock.id)
            else:
                status = False
                break
        """End NSE Block"""
        if status:
            response_object = {
                'status': 'success',
                'message': 'Stock report successfully imported from NSE/BSE'
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 500

class ImportDailyStockReport(Resource):
    @admin_token_required
    def get(self):
        """Import stock daily data and store into database"""
        """Start NSE Block"""
        downloaded_response = requests.get(ExternalCSV.NSE_DAILY_STOCK_REPORT)
        csv_reader = csv.reader(downloaded_response.content.decode('utf-8').splitlines(), delimiter=',')
        status = save_dly_stk_rpt_nse(csv_reader)
        """End NSE Block"""
        if status:
            respoonse_object = {
                'status': 'success',
                'message': 'Stock report successfully imported from NSE/BSE'
            }
            return respoonse_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return respoonse_object, 500