import time
import csv
import datetime
import math
from pykrx import stock

#list_ = [51600, 52600, 52500, 52800, 53700, 53500, 53500, 52000, 51000, 51600, 51800, 51800, 52200, 51300, 50300, 50400, 49900, 49450, 49500, 50400, 51200, 51500, 51900, 53300, 54700, 54700, 56700, 56300, 56000, 56000, 55500, 55000, 55400, 56500, 55800, 55200, 55500, 55500, 55800, 56800, 58600, 59500, 60000, 60000, 59000, 60700, 61300, 62400, 61400, 62300]



list_ = stock.get_market_ohlcv_by_date("20200101", "20200125", "005380")

def WMA(df, period): # 가중이동평균
    result = []
    for epoch in range(len(df) - period+1):
        value = 0
        for n in range(1, period+1):
            value = value + (df[n+epoch-1] * n)
        result.append(value / ((period * (period + 1)) / 2))
    return result

def HMA(df, period): # Hull 이동평균
    data1 = WMA(df, int(period/2))
    for i in range(0, len(data1)):
        data1[i] = data1[i] * 2
    data2 = WMA(df, period)
    data3 = []
    for i in range(0, len(data2)):
        data3.append(data1[i + len(data1) - len(data2)] - data2[i])
    return (WMA(data3, int(math.sqrt(period))))


print(HMA(list_,11))


