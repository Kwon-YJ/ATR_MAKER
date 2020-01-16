#from pandas_datareader import data
from datetime import datetime
from pykrx import stock
#import csv
import time

Result = []

now = datetime.now()

Start_Day = "1996-05-06"

End_Day = ('%s%s%s' % (now.year, now.month, now.day))

           
           
#End_Day = ('%s-%s-%s' % (now.year, now.month, now.day))
#Today = ("%s%s%s", % (now.year, now.month, now.day))




'''
print(stock.get_market_ticker_list()[15])
a = stock.get_market_ticker_list()
print(stock.get_market_ohlcv_by_date("20180810", "20181212", stock.get_market_ticker_list()[15]))




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
'''

bugList = []

epoch = 0

for ticker in stock.get_market_ticker_list():
	time.sleep(1)
	df = stock.get_market_ohlcv_by_date("20000101", "20200116", ticker)
	try:
		if float(max(df['종가'])) == float(df['종가'].tail(1)):
			Result.append(stock.get_market_ticker_name(stock))
	except:
		bugList.append(ticker)
	print(epoch)
	epoch = epoch + 1

print(bugList)
print(Result)

'''
df = data.DataReader("005930.KS", 'yahoo', Start_Day, End_Day)

print(float(max(df['Adj Close'])))

print(float(df['Adj Close'].tail(1)))

if float(max(df['Adj Close'])) == float(df['Adj Close'].tail(1)):
    print("예스")
'''
