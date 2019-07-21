from django.core.management.base import BaseCommand, CommandError
from rank.models import Coin
import ccxt
import time

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
    for symbol in exchange.markets:
        if symbol == coin.ieoname + "/USDT":
            time.sleep(exchange.rateLimit / 1000)
            history = exchange.fetchOHLCV(symbol, '1d')
