from flask import Response
import requests
import time

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.nseindia.com/get-quotes/equity?symbol=TCS',
    'Host': 'www.nseindia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def index():
    def events():
        while True:
            download_content = requests.get(url="https://www.nseindia.com/api/quote-equity?symbol=TCS", headers=headers)
            stock_json = download_content.json()
            response_json = {
                'status': 'success',
                'data': {
                    'low_price': '',
                    'high_price': '',
                    'last_price': '',
                    'avg_price': '',
                }
            }
            yield 'test\n'
            time.sleep(60)  # an artificial delay
    return Response(events(), content_type='json/event-stream')
