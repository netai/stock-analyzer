import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
from app.constants import ExternalURL

class NSEHelper:
    """Process the NSE data from NSE website"""

    def __init__(self):
        self.formData = {
            '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$lnkDownload',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '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'
        }

    def get_stock_list(self):
        """Import stock list from BSE website"""
        stock_list = []
        try:
            downloaded_response = requests.get(ExternalURL.BSE['STOCK_LIST'])
            csv_reader = csv.reader(downloaded_response.content.decode('utf-8').splitlines(), delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                stock_list.append({
                    'symbol': row[2].strip(),
                    'company_name': row[3].strip(),
                    'series': row[9].strip()[:2],
                    'isin_number': row[7].strip(),
                    'face_value': row[6].strip(),
                    'exchange_name': 'BSE'
                })
            
            return stock_list

        except Exception as e:
            print(e)
            return None

    def get_history_report(self, symbol):
        """Import stock history data from NSE website"""
        history_data = []
        try:
            symbol_count_response = requests.get(url=ExternalURL.NSE['SYMBOL_COUNT'].format(symbol=requests.utils.quote(symbol)), headers=self.headers)
            downloaded_response = requests.get(ExternalURL.NSE['HISTORY_REPORT'].format(symbol=requests.utils.quote(symbol), symbolCount=symbol_count_response.text.strip()), headers=self.headers)
            soup = BeautifulSoup(downloaded_response.text, 'html.parser')
            content_obj = soup.find('div', id='csvContentDiv')
            if content_obj:
                csv_content = content_obj.text.split(':')
                csv_reader = csv.reader(csv_content, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    if row:
                        traded_qty = ('' if row[10].strip()=='-' else row[10].strip())
                        delv_qty = ('' if row[13].strip()=='-' else row[13].strip())
                        delv_per = ('' if row[14].strip()=='-' else row[14].strip())
                        history_data.append({
                            'symbol': row[0].strip(),
                            'series': row[1].strip(),
                            'date': datetime.strptime(row[2].strip(), "%d-%b-%Y").date(),
                            'prev_price': row[3].strip(),
                            'open_price': row[4].strip(),
                            'high_price': row[5].strip(),
                            'low_price': row[6].strip(),
                            'last_price': row[7].strip(),
                            'close_price': row[8].strip(),
                            'avg_price': row[9].strip(),
                            'traded_qty': traded_qty,
                            'delivery_qty': delv_qty,
                            'delivery_per': delv_per,
                            'exchange_name': 'NSE',
                            'trade_timeframe': '1D'
                        })
                    
            return history_data

        except Exception as e:
            print(e)
            return None

    def get_daily_report(self):
        """Import daily report from NSE website"""
        daily_data = []
        try:
            downloaded_response = requests.get(ExternalURL.NSE['DAILY_REPORT'])
            csv_reader = csv.reader(downloaded_response.content.decode('utf-8').splitlines(), delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if row:
                    traded_qty = ('' if row[10].strip()=='-' else row[10].strip())
                    delv_qty = ('' if row[13].strip()=='-' else row[13].strip())
                    delv_per = ('' if row[13].strip()=='-' else row[14].strip())
                    daily_data.append({
                        'symbol': row[0].strip(),
                        'series': row[1].strip(),
                        'date': datetime.strptime(row[2].strip(), "%d-%b-%Y").date(),
                        'prev_price': row[3].strip(),
                        'open_price': row[4].strip(),
                        'high_price': row[5].strip(),
                        'low_price': row[6].strip(),
                        'last_price': row[7].strip(),
                        'close_price': row[8].strip(),
                        'avg_price': row[9].strip(),
                        'traded_qty': traded_qty,
                        'delivery_qty': delv_qty,
                        'delivery_per': delv_per,
                        'exchange_name': 'NSE',
                        'trade_timeframe': '1D'
                    })

            return daily_data

        except Exception as e:
            print(e)
            return None