from flask_restful import Resource
import csv
import requests
from bs4 import BeautifulSoup
from ..util.decorator import admin_token_required
from ..helpers.import_helper import save_stk_nse, save_stk_rpt_nse, save_dly_stk_rpt_nse
from ..helpers.stock_helper import get_all_stock
from app.constants import ExternalCSV

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
            'Cookie': 'sym1=TCS; sym2=WIPRO; _ga=GA1.2.270553252.1586297590; sym3=WSTCSTPAPR; pointer=3; NSE-TEST-1=1910513674.20480.0000; JSESSIONID=32B5753785DD9D53657AAA8963C0A520.jvm1; bm_mi=CDAB10079ED92C19E38216AC6A9E7196~KhR3Kh7Cjdq1AG1kpvs03fl7UD2G81qHGyfhDRPYpW4qzLcNhD6gFcxwxUtfWpzZOt5Hq9SVnNDB5WNXcoZVApyaoy9ii5Mf64BM7cV4ZoqEPpnr28zkGiJh1sMK02En/Cc2BgKVz81w5LxvxVIxESMdxYPFWJ2o2yWokjA+LT1+zvLcdf7r6Xi4AfhWo06j28z0M+5HNgvY7mcd7MmJ6TjoUQOySrcq+l4EChZ5RWIi8XZhf2ysNLHw4ambjiM99N/yk/FsEk2MsQ4+xP7VmSLSSwIsNiNzFsW9g+S4ToL46DUjBh8SjQelLQPgpVb5+hWRcw1oB/f0h3DQU+AdVsdPNaRC5x2qJROG8ySeBAA=; ak_bmsc=3624F46499D11F36FBAC5CFDBF8331A650434A65F1010000BCE7915EB4829E78~plp2Wkyfr6HMqmNwKUMCNvlOnbw/L9L69FU0xi2HpK8w5cKEjdv8f2ywYYIbLKcyZMIowcb3QvwtXj6C2WudxyiHiN11c+r75snnRTF6c28fcPfHaiAuAAF/0ShiTvsAxIiZEyfjaLWAao6QolRPoQalBt+/xATiE0Q6Dl+5yXvsWW0NbiyWoZ8lW88eZ/wrm37k/duf1d2i/va2+hgiutsYZn4U8BhWqQ5jI7rpZXAQxoiRzv+6Sgu/PAILmotRJh; RT="z=1&dm=nseindia.com&si=ce6a7f89-dc0d-4870-a97e-07dbe084f7ff&ss=k8vnuvtf&sl=0&tt=0&bcn=%2F%2F684fc53f.akstat.io%2F"; bm_sv=2422D560D37AB411EA5448658F86C589~oM5yD+DWZiac7gAFtg9xSF7avSFRy/k+rlNbwuAjjLKXA1ZsnBEvuVjBPQtVIAnGeusdj4njm2ksDnD049H31RxaAY7HehuFpb8yMfMuMBMBHIb7OX8dIqwqpV9xJGDycAbFeMzflsy0c2wY+iGTdetQT6H8KB827VDLU5wJdIo=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        status = False
        stock_list = get_all_stock()
        for stock in stock_list:
            if stock.id < 329:
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