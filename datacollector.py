import pandas as pd
import requests
import os

AV_APIKEY = os.environ["AV_APIKEY"]

slices = ["year1month1","year1month2", "year1month3", "year1month4", "year1month5", "year1month6", "year1month7", "year1month8", "year1month9", "year1month10", "year1month11", "year1month12", "year2month1", "year2month2", "year2month3", "year2month4", "year2month5", "year2month6", "year2month7", "year2month8", "year2month9", "year2month10", "year2month11", "year2month12"]

def main():
    symbols = get_symbols()
    print(symbols[0])

def get_data(symbol, slice):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval=1min&slice={slice}&apikey={AV_APIKEY}'
    r = requests.get(url)
    data = r.json()



def get_symbols():
    symbols_table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", header=0)[0]
    symbols = list(symbols_table.loc[:, "Symbol"])
    return symbols


if __name__ == "__main__":
    main()
