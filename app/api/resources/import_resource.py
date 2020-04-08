from flask_restful import Resource
import csv
import requests
from bs4 import BeautifulSoup
from ..util.decorator import admin_token_required
from ..helpers.import_helper import save_stock_from_nse, save_stock_report_from_nse
from ..helpers.stock_helper import get_all_stock
from ..constants import ExternalCSV

class ImportStock(Resource):
    @admin_token_required
    def get(self):
        """Import stocks from nse/bse website and store into database"""
        """Start NSE Block"""
        downloaded_response = requests.get(ExternalCSV.NSE_STOCK_LIST)
        csv_reader = csv.reader(downloaded_response.content.decode('utf-8').splitlines(), delimiter=',')
        status = save_stock_from_nse(csv_reader)
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
            'Cookie': 'sym1=TCS; sym2=WIPRO; _ga=GA1.2.270553252.1586297590; _gid=GA1.2.1878695094.1586297590; sym3=WSTCSTPAPR; pointer=3; NSE-TEST-1=1910513674.20480.0000; RT="z=1&dm=nseindia.com&si=ce6a7f89-dc0d-4870-a97e-07dbe084f7ff&ss=k8rnijjh&sl=0&tt=0&bcn=%2F%2F684fc538.akstat.io%2F"; ak_bmsc=2CEF79D12ABA7637AAB6A1CC82C94EB4172F951D6851000077308E5E27701A24~plEmXAzwU5adlWMzuC7m7Ys/Fc/CCWJj5EcksKgI1JJFuvtybwmhthnh57Fs/1aeNGi9IieRELjBXdvR26sB4+S1Dz7AM5ubDsGs0+4Q7B4gqmMY15P+RJVxfV2kt11DDl3St7BJ0B9np59CLCGN1QVUYFlUZPbLeE8fdOuFl8WqcauC8TozzkyklcF/zpm4av5eD51Li8cW+x0G4qdYqFIeKO9Oe3km7qPFswup7uLb0=; JSESSIONID=B35BA025CAAF8EB0B9668DFCF27E0EF5.tomcat2; bm_mi=6B25F8913D8081F829DFD6052B017257~UIZO9HxJzqcQWCxoTQtSKVfhuWzgpYKdK6tKTHG8rarYhrZ/cE3MDQAZBlUc/e2nNGAaBHmp2wI6Fw/izTSebpcFOFDSxcpNRe4/j3vLULSKNnMD63e5MuSqpESfgrP6h9UVORoE5WguaTEgNWTi94zF4gabff3A9S4637p5bDZ1zJwxTt1TB25fk9vnri8L33mQBKr/6SMIWapYye4gPhFTac6by/cFZJ5Ffc0LlJQneR/63ifMvaMuzs7FlUEqR3MXSzVh9igaOiN0ff1QEQ==; bm_sv=FE3AA0353A72F2C07351941AFED24E48~KkqnBWXxBZNwIh7CnuwGJ61473kLZKnrK//y8Y8/420o+RwyJIgKwVJJ77+kOgGgsGwmA85n/e2MU2o0NCGarlarLxBuVWiXXVxfQ7RO0Mv8hq2/eJlFMlAZfgDbVKSP5WY9QufiFf8mJIs56Olkoi3j+E/B0dZPCxm0b9qWuqM=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        status = False
        stock_list = get_all_stock()
        for stock in stock_list:
            if stock.id < 100:
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
                status = save_stock_report_from_nse(csv_reader, stock.id)
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

