import django_tables2 as tables
from .models import Coin

class CoinTable(tables.Table):
    class Meta:
        model = Coin
        template_name = 'django_tables2/bootstrap.html'
