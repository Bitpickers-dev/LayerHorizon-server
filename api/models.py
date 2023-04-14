from django.db import models


class EthBlock(models.Model):
    number = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    transactions = models.JSONField()

    class Meta:
        ordering = ['-number']
