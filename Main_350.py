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

tickers = ["000070","000080","000100","000120","000150","000210","000240","000250","000270","000640","000660","000670","000720","000810","000880","000990","001040","001060","001120","001230","001430","001450","001520","001680","001740","001800","002240","002270","002350","002380","002790","002960","003000","003240","003380","003410","003490","003520","003550","003620","003850","003920","004000","004020","004170","004370","004490","004800","004990","005180","005250","005290","005300","005380","005440","005490","005610","005830","005850","005930","005940","006120","006260","006280","006360","006390","006400","006650","006730","006800","006840","007070","007310","007390","007570","007820","008060","008560","008770","008930","009150","009240","009420","009540","009830","010060","010120","010130","010140","010620","010780","010950","011070","011170","011210","011780","011790","012330","012450","012630","012750","013030","014620","014680","014820","014830","015750","015760","016250","016360","017670","017800","018250","018260","018880","019210","019680","020000","020150","021240","022100","023160","023410","023530","024110","025540","025860","025900","025980","026960","027410","028050","028150","028260","028300","028670","029780","029960","030000","030190","030200","030530","031390","031430","032500","032640","032830","033290","033640","033780","034020","034220","034230","034730","035250","035420","035600","035720","035760","035810","035890","035900","036460","036490","036540","036570","036630","036830","036930","038500","039030","039200","039840","041140","041510","041830","041960","042000","042660","042670","043150","044340","044490","045100","045390","046890","047040","047050","047310","047810","048260","048410","048530","049770","049950","051500","051600","051900","051910","052020","052690","053800","055550","056190","057050","058470","058820","060150","060250","060570","060980","061970","063570","064350","064760","064960","065620","065660","066570","066970","067160","067390","067630","068240","068270","068760","069080","069260","069620","069960","071050","071840","073070","073240","078130","078160","078340","078930","079160","079430","079550","080160","081660","082270","083790","084110","084990","086280","086450","086520","086790","086900","088350","089600","090430","090460","091700","091990","092040","092730","093050","093370","095190","095610","095700","096530","096760","096770","097520","097950","098460","103140","104830","105560","105630","108230","108320","108670","111770","112040","114090","115390","115450","115960","120110","122870","122990","128940","138080","138930","139480","140410","141080","143240","144510","145020","145990","161390","161890","170900","178320","178920","182400","183490","185750","192400","192440","192820","196170","200130","200230","204320","207940","213420","214150","214320","214450","215000","215200","215360","215600","217730","218410","222040","228760","230360","237690","237880","239610","240810","241560","243070","243840","247540","251270","253450","263050","263750","265520","267250","267980","271560","272290","278280","282330","285130","294870","298040","298380","316140"]

Output_List = []

# 종목명 - 금일종가 - ATR - ATR/금일종가

for i in range(len(tickers)):
    try:
        try:
            df = data.DataReader(tickers[i]+".KS",'yahoo', Start_Day, End_Day)
            atr = get_ATR(df)
            Output_List.append(stock.get_market_ticker_name(tickers[i]))
            Close_ = ((df["Close"]).head(1)).values
            Output_List.append(str(Close_)[1:-1])
            Output_List.append(str(atr)[1:-1])
            Output_List.append((str(float(atr) / Close_))[1:-1])

        except:
            df = data.DataReader(tickers[i]+".KQ",'yahoo', Start_Day, End_Day)
            atr = get_ATR(df)
            Output_List.append(stock.get_market_ticker_name(tickers[i]))
            Close_ = ((df["Close"]).head(1)).values
            Output_List.append(str(Close_)[1:-1])
            Output_List.append(str(atr)[1:-1])
            Output_List.append((str(float(atr) / Close_))[1:-1])
    except:
        print("")
    if i%5==0:
        print(i)
        
f = open('write.csv','w',encoding="euc-kr", newline='')
wr = csv.writer(f)
try:
    i = 0
    while(len(Output_List)):
        if i==0:
            wr.writerow(["종목명", "금일종가", "ATR", "ATR/금일종가"])
        wr.writerow([Output_List[i], Output_List[i+1], Output_List[i+2], Output_List[i+3]])
        i = i+4
except:
    print("프로그램 실행 완료")
f.close()


