# -*- coding: utf-8 -*- 
#from pandas_datareader import data
from datetime import datetime
from pykrx import stock
import time
#import telegram


#my_token = "888909254:AAFhueNYmy65PCZrn0EI5OQA4vFq6Fk5MfI"
#bot = telegram.Bot(token = my_token)


konex = []
tickers = list(set(stock.get_market_ticker_list()) - set(konex))


Result = []
bugList = []
now = datetime.now()
Today = ('%s%s%s' % (now.year, now.month, now.day))
if len(Today) != 8:
    Today = str(Today[0:4]) + '0' + str(Today[4:7])
while(True):
    #epoch = 0
    #for ticker in stock.get_market_ticker_list():
    for ticker in tickers:
        time.sleep(1.5)
        df = stock.get_market_ohlcv_by_date("20000101", Today, ticker)
        try:
            if float(max(df['종가'])) == float(df['종가'].tail(1)):
                Result.append(ticker)
                Result.append(stock.get_market_ticker_name(ticker))
        except:
            bugList.append(ticker)
        #print(epoch)
        #epoch = epoch + 1
    #bot.send_message(chat_id = 801167350, text = str(bugList))
    #bot.send_message(chat_id = 801167350, text = str(Result))
    print(Result)

    '''
    while(true):
        reset_time = ('%s' % (now.hour))
        if reset_time == 18:
            break
        else:
            time.sleep(1500)
'''
#습작-------------------------------------------------------------------

'''
#End_Day = ('%s-%s-%s' % (now.year, now.month, now.day))
#Today = ("%s%s%s", % (now.year, now.month, now.day))

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
ddddddddddd

df = data.DataReader("005930.KS", 'yahoo', Start_Day, End_Day)

print(float(max(df['Adj Close'])))

print(float(df['Adj Close'].tail(1)))

if float(max(df['Adj Close'])) == float(df['Adj Close'].tail(1)):
    print("예스")

df = stock.get_market_ohlcv_by_date("20000101", "20200116", '281820')

print(float(max(df['종가'])))

print(float(df['종가'].tail(1)))
'''
