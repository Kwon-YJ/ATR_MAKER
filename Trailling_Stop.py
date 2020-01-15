from pandas_datareader import data
from datetime import datetime 
from pykrx import stock
import csv

def day_ago(day,ohlcv,ticker):
    a = ticker.tail(day)
    b = a[ohlcv]
    c = b.head(1)
    return c

def get_TR(date,ticker):
    a = day_ago(date,'High',ticker)
    b = day_ago(date,'Low',ticker)
    c = a.values-b.values

    aa = day_ago(date,'High',ticker)
    bb = day_ago(date+1,'Close',ticker)
    cc = abs(aa.values-bb.values)

    aaa = day_ago(date,'Low',ticker)
    bbb = day_ago(date+1,'Close',ticker)
    ccc = abs(aaa.values-bbb.values)

    return max(c,cc,ccc)

def get_ATR(ticker):
    value = 0
    for i in range(15):
        TR = get_TR(i+2,ticker)
        value = value + TR
    return value/15

now = datetime.now()

Start_Day = ('%s-%s-%s'%(now.year, now.month, now.day-20))
End_Day = ('%s-%s-%s'%(now.year, now.month, now.day))

tickers = ["036540","000990","067900","097520","290740","068290","101490","010640","033660"]
Buy_Day = ["2019-12-23", "2019-12-23", "2019-12-23", "2019-12-23", "2019-12-23", "2019-12-23", "2019-12-23", "2019-12-24", "2019-12-24"]

Output_List = []

# 종목명 - 금일종가 - ATR - ATR/금일종가

# 종목명 - 금일종가 - 고가 - ATR - 손절가 (매수일 이후로부터 최고가 - 3ATR)

for i in range(len(tickers)):
	try:
		try:
			df = data.DataReader(tickers[i]+".KS",'yahoo', Start_Day, End_Day)
			df2 = data.DataReader(tickers[i]+".KS",'yahoo', Buy_Day[i], End_Day)
			High = (df2["High"].max(axis=0).max())
			Close_ = ((df["Close"]).tail(1)).values
			atr = get_ATR(df)
			stop = (float(High))-(3*float(atr))
			Output_List.append(stock.get_market_ticker_name(tickers[i]))
			Output_List.append(str(Close_)[1:-1])
			Output_List.append(stop)
			print(stop)
		except:
			df = data.DataReader(tickers[i]+".KQ",'yahoo', Start_Day, End_Day)
			df2 = data.DataReader(tickers[i]+".KQ",'yahoo', Buy_Day[i], End_Day)
			High = (df2["High"].max(axis=0).max())
			Close_ = ((df["Close"]).tail(1)).values
			atr = get_ATR(df)
			stop = (float(High))-(3*float(atr))
			Output_List.append(stock.get_market_ticker_name(tickers[i]))
			Output_List.append(str(Close_)[1:-1])
			Output_List.append(stop)
			print(stop)
	except:
			print("")
	if i%5==0:
		print(i)
		
		
		
print(Output_List)



# 종목명 - 금일종가 - 고가 - ATR - 손절가 (매수일 이후로부터 최고가 - 3ATR)
f = open('write.csv','w',encoding="euc-kr", newline='')
wr = csv.writer(f)
try:
    i = 0
    while(len(Output_List)):
        if i==0:
            wr.writerow(["종목명", "금일종가", "손절가"])
        wr.writerow([Output_List[i], Output_List[i+1], Output_List[i+2]])
        i = i+3
except:
    print("프로그램 실행 완료")
f.close()
