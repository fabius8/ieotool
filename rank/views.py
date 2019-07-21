from django.shortcuts import render

from django_tables2 import RequestConfig

# Create your views here.
from .models import Coin
from .tables import CoinTable


def coin(request):
    table = CoinTable(Coin.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'rank/coin.html', {'table': table})
