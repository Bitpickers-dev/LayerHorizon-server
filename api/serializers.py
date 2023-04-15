from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api import models


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EthBlockSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.EthBlock
        fields = ['number', 'hash', 'timestamp', 'count', 'transactions']


class ArbBlockSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.ArbBlock
        fields = ['number', 'hash', 'timestamp', 'count', 'l1BlockNumber', 'transactions']


class OptBlockSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.OptBlock
        fields = ['number', 'hash', 'timestamp', 'count', 'l1BlockNumber', 'transactions']
