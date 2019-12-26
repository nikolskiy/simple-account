from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('uuid', 'name', 'balance', 'hold', 'status')


class InfoSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(format='hex_verbose')


class UpdateSerializer(InfoSerializer):
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
