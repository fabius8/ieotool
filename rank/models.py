from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=100, verbose_name='币种')
    ieotime_date = models.DateField(verbose_name='上市日期')
    ieoexchange = models.CharField(max_length=100, verbose_name='交易所')
    ieocost = models.FloatField(verbose_name='IEO成本')
    ieoprice = models.FloatField(verbose_name='现价', default=0.0)
    ieohighprice = models.FloatField(verbose_name='最高价', default=0.0)
    ieohighestuppercent = models.FloatField(verbose_name='最高涨幅', default=0)
    ieocurrentuppercent = models.FloatField(verbose_name='现价涨幅', default=0)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

#class Update(models.Model):

