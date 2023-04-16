from django.db import models

class MarketData(models.Model):
    symbol = models.CharField(max_length=20)
    expiry = models.DateField()
    underlying = models.CharField(max_length=100)
    spot_price = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=6, decimal_places=4)
    volatility = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return f"{self.symbol} - {self.expiry}"

class Option(models.Model):
    market_data = models.ForeignKey(MarketData,related_name='market_name', on_delete=models.CASCADE)
    type = models.CharField(max_length=4)
    strike = models.DecimalField(max_digits=10, decimal_places=2)
    pv = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.market_data.symbol} {self.type} {self.market_data.underlying} Strike {self.strike}"


