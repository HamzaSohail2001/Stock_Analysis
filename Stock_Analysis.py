import requests

Stock_ID = "TSLA"
key = "2179439393b44271aedef922be51bbe5"


def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


stockdata = get_stock_quote(Stock_ID, key)
stock_price = get_stock_price(Stock_ID, key)

name = stockdata['name']

print(name, stock_price)
