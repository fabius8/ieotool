from django.core.management.base import BaseCommand, CommandError
from rank.models import Coin
import ccxt
import time
import datetime

binance = ccxt.binance()
binance.load_markets()
okex = ccxt.okex()
okex.load_markets()
huobi = ccxt.huobi()
huobi.load_markets()

# if binance.has['fetchOHLCV']:
#     for symbol in binance.markets:
#         if symbol == "BTC/USDT":
#             time.sleep(binance.rateLimit / 1000)
#             print(symbol, binance.fetch_ohlcv(symbol,'1d'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        for coin in Coin.objects.all():
            if coin.ieoexchange == 'binance':
                update_coin(coin, binance)
            if coin.ieoexchange == 'okex':
                update_coin(coin, okex)
            if coin.ieoexchange == 'huobi':
                update_coin(coin, huobi)

def update_coin(coin, exchange):
    print("update coin ", coin.name)
    for symbol in exchange.markets:
        if symbol == coin.name + "/USDT":
            time.sleep(exchange.rateLimit / 1000)
            history = exchange.fetchOHLCV(symbol, '1d', 1546272000000)
            listhighest = []
            for item in history:
                listhighest.append(item[2])
            # highest price
            coin.ieohighprice = max(listhighest)
            # Now price
            coin.ieoprice = history[-1][4]
            # IEO time
            coin.ieotime_date = datetime.datetime.fromtimestamp(history[0][0]/1000)
            coin.ieohighestuppercent = float(coin.ieohighprice) / coin.ieocost
            coin.ieocurrentuppercent = float(coin.ieoprice) / coin.ieocost
            coin.save()
