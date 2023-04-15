from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EthBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EthBlock
        fields = ['number', 'hash', 'timestamp', 'count', 'transactions']


class ArbBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ArbBlock
        fields = ['number', 'hash', 'timestamp', 'count', 'l1BlockNumber', 'transactions']


class OptBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OptBlock
        fields = ['number', 'hash', 'timestamp', 'count', 'l1BlockNumber', 'transactions']
