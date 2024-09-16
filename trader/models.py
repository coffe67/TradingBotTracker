from django.db import models


class SymbolPrice(models.Model):
    symbol = models.CharField(max_length=100, help_text='Par name of the asset, ex.. BTC-USD')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class TradeAlert(models.Model):
    symbol = models.CharField(max_length=100, help_text='Par name of the asset, ex.. BTC-USD')
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=75)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
