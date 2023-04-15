from django.db import models


class EthBlock(models.Model):
    number = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    count = models.IntegerField()
    transactions = models.JSONField()

    class Meta:
        ordering = ['-number']


class ArbBlock(models.Model):
    number = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    count = models.IntegerField()
    l1BlockNumber = models.CharField(max_length=255)
    transactions = models.JSONField()

    class Meta:
        ordering = ['-number']


class OptBlock(models.Model):
    number = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    count = models.IntegerField()
    l1BlockNumber = models.CharField(max_length=255)
    transactions = models.JSONField()

    class Meta:
        ordering = ['-number']
