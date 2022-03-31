from .models import Trader, Stock
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock

    def create(self, validated_data):
        stock = Stock.objects.create(**validated_data)
        return stock


class TraderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trader

    def create(self, validated_data):
        trader = Trader.objects.create(**validated_data)
        return trader