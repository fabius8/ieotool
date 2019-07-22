from django.shortcuts import render

from django_tables2 import RequestConfig

# Create your views here.
from .models import Coin
from .tables import CoinTable


def coin(request):
    table = CoinTable(Coin.objects.all(), exclude='time')
    RequestConfig(request).configure(table)
    updatetime = Coin.objects.all().first().time
    print(updatetime)
    return render(request, 'rank/coin.html', {
        'table': table,
        'time': updatetime
    })
