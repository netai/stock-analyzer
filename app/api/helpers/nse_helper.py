import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
from app.constants import ExternalURL

class NSEHelper:
    """Process the NSE data from NSE website"""

    def __init__(self):
        self.headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www1.nseindia.com/products/content/equities/equities/eq_security.htm',
                'Host': 'www1.nseindia.com',
                'Cookie': 'sym1=TCS; sym2=WIPRO; _ga=GA1.2.270553252.1586297590; sym3=WSTCSTPAPR; pointer=3; pointerfo=1; instrument1=OPTSTK; underlying1=ACC; expiry1=; optiontype1=PE; strikeprice1=1100.00; JSESSIONID=D5D76D272D4064A2E48F9283A6D02A26.tomcat2; NSE-TEST-1=1927290890.20480.0000; ak_bmsc=250E97FFABCA3E1D1F6D83273626598817372F0E3C6700003264A05E793B1C3D~plo9R8FIgdn6X1N+PhMbKaDu83+izs9BMu3Vrei45iM0tSHrghiXg8i/kJJWbXOpMqyP9Yycg6yPMH78H4fmnXoHX5hR9Ktatxp9bXLh4o7axWlSgMRj6dyeNUcHKEbinwudnDy0WSxdHu/DVZUYCsnobLXdBP2K36MC3d8isnY1/h53L+iFQMz4/SfZTZ7cJzyv8eV449xTzgf6S3DISg8gXlQyrI0Umn24J4ajDjTiE=; RT="z=1&dm=nseindia.com&si=ce6a7f89-dc0d-4870-a97e-07dbe084f7ff&ss=k9bhu0f2&sl=5&tt=no&obo=2"; bm_mi=5BEC2D29C5F8439EBD5607208FA7F6F4~dr8a8CICHII4jP8Fb6FR2tCEVeaG4CrB+Ot6P8lpgko0z2OgVy6ZZt9cDD6Wo3y5EdjZo1X/2EXuFnBF0CfNuaHeIGI+ET7EacxQmRH+2wZQpwcXDx5sQ+Sf686dyINyXKOo7c7JSbYBky80x0Xm6ShwTaIJsJUeudZrHr9lMyQ4mz+nl5TdNv1zrltvZHF72ap0RF9LjAM2aOJa/Y5Pwe1KfWnpxlcV6JO0/XDbM2frOnFaQ5zYkiBprKFYvcW8wf+eX/rV5XGAUgLu+giviw==; bm_sv=D7A134B8096FCFCDC582B6BFCE24198A~WjgerT6K2+k38iTjHV+N6KyIFjPH3K+rNNptrS/lh+qiLpRZe5+BtNp++PNPP5Tzj3b6xBpGkBqKvZLPK3Yp54qMkUre3kxblTsGNJmqHZQh2ZDNZhVDz2msr+yJdYFsPnRkT2UewFDp7hbvih/1X06FBa4XyDnIa0VRob/kwa0=',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

    def get_stock_list(self):
        """Import stock list from NSE website"""
        stock_list = []
        try:
            downloaded_response = requests.get(ExternalURL.NSE['STOCK_LIST'])
            csv_reader = csv.reader(downloaded_response.content.decode('utf-8').splitlines(), delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                stock_list.append({
                    'symbol': row[0].strip(),
                    'company_name': row[1].strip(),
                    'series': row[2].strip(),
                    'listing_date': datetime.strptime(row[3].strip(), "%d-%b-%Y"),
                    'isin_number': row[6].strip(),
                    'face_value': row[7].strip(),
                    'exchange_name': 'NSE'
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

    def get_symbol_change_list(self):
        """Import symbol change list from NSE website"""
        symbol_list = []
        try:
            downloaded_response = requests.get(ExternalURL.NSE['SYMBOL_CHANGE'])
            csv_reader = csv.reader(downloaded_response.content.decode('cp1252').splitlines(), delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                symbol_list.append({
                    'old_symbol': row[1].strip(),
                    'new_symbol': row[2].strip(),
                    'company_name': row[0].strip(),
                    'date': datetime.strptime(row[3].strip(), "%d-%b-%Y"),
                    'exchange_name': 'NSE'
                })
            
            return symbol_list

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