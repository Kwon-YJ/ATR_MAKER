# -*- coding: utf-8 -*- 
#from pandas_datareader import data
from datetime import datetime
from pykrx import stock
import time
import telegram


my_token = "888909254:AAFhueNYmy65PCZrn0EI5OQA4vFq6Fk5MfI"
bot = telegram.Bot(token = my_token)


konex = ['341310','179530','336040','331660','337840','093510','327970','329050','309900','317860','323350','311840','314130','308700','311060','303360','271780','279060','302920','276240','299480','299670','163430','288490','285770','281310','236030','284420','277880','278990','270020','267060','270660','270210','271850','224880','266170','267810','266870','225860','284610','278380','242350','258250','258540','232830','243870','251280','251960','239890','191600','246250','245450','208850','224020','244880','112190','241510','238500','217910','212310','222160','250030','240340','327610','236340','232530','215570','233990','232680','211050','227420','229500','228180','229000','224760','223220','233250','238170','252370','149300','221800','217880','258050','222670','220110','225220','215050','217950','205290','208890','214610','140610','200580','203400','206950','200350','217320','178600','189330','189540','189350','183350','150440','179720','086080','260870','158300','180060','140290','120780','210120','084440','121060','140660','216280','058970','207490','234070','260970','224810','149010','185190','126340','199290','225850','162120','176750','183410','199150','135160','076340','107640','136660','220250','103660','114920','216400','116100','101360','202960','199800','066830','148780','092590','064850','044990','086460','067370','086220']
tickers = list(set(stock.get_market_ticker_list()) - set(konex))


Result = []
bugList = []
now = datetime.now()
Today = ('%s%s%s' % (now.year, now.month, now.day))
if len(Today) != 8:
    Today = str(Today[0:4]) + '0' + str(Today[4:7])
while(True):
    for ticker in tickers:
        time.sleep(1.5)
        df = stock.get_market_ohlcv_by_date("20000101", Today, ticker)
        try:
            if float(max(df['종가'])) == float(df['종가'].tail(1)):
                Result.append(stock.get_market_ticker_name(ticker))
        except:
            bugList.append(ticker)
    
    #bot.send_message(chat_id = 801167350, text = str(bugList))
    #bot.send_message(chat_id = 801167350, text = str(Result))
    matching = [s for s in Result if "스팩" in s]
    #print(list(set(Result) - set(matching)))
    bot.send_message(chat_id = 801167350, text = str(list(set(Result) - set(matching))))
    while(true):
        reset_time = ('%s' % (now.hour))
        if reset_time == 18:
            break
        else:
            time.sleep(1500)

