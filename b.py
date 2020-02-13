from pykrx import stock

df = stock.get_market_ohlcv_by_date("20180810", "20181212", "005930", "m")
print(df.head(3))