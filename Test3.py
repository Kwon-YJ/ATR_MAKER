from pandas_datareader import data
from datetime import datetime
from pykrx import stock
#import csv

#tickers = stock.get_market_ticker_list()

Result = []

now = datetime.now()

Start_Day = "1996-05-06"

End_Day = ('%s-%s-%s' % (now.year, now.month, now.day))

tickers = stock.get_market_ticker_list()

for i in range(len(tickers)):
    try:
        try:
            df = data.DataReader(tickers[i] + ".KS", 'yahoo', Start_Day, End_Day)
            if float(max(df['Adj Close'])) == float(df['Adj Close'].tail(1)):
                Result.append(stock.get_market_ticker_name(tickers[i]))
        except:
            df = data.DataReader(tickers[i] + ".KQ", 'yahoo', Start_Day, End_Day)
            if float(max(df['Adj Close'])) == float(df['Adj Close'].tail(1)):
                Result.append(stock.get_market_ticker_name(tickers[i]))
    except:
        print("")
    if i % 5 == 0:
        print(i)

print(Result)





'''
df = data.DataReader("005930.KS", 'yahoo', Start_Day, End_Day)

print(float(max(df['Adj Close'])))

print(float(df['Adj Close'].tail(1)))

if float(max(df['Adj Close'])) == float(df['Adj Close'].tail(1)):
    print("예스")
'''