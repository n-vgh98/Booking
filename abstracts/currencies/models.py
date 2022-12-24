from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=4)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        return super(Currency, self).save(self, *args, **kwargs)


class CurrencyExchangeRate(models.Model):
    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_from_change')
    currency_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_to_change')
    rate = models.FloatField()
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('currency_from', 'currency_to'), name='unique_currency_from_currency_to'),
            models.CheckConstraint(
                check=~models.Q(currency_from=models.F('currency_to')),
                name='currency_from_and_currency_to_not_be_equal')
        ]
