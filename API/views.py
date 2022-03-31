from __future__ import unicode_literals
from django.shortcuts import render
from .models import Trader, Stock
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from django.http import Http404
from .serializers import StockSerializer, TraderSerializer
from itertools import groupby
from datetime import date, timedelta, datetime
from dateutil.parser import parse
import collections


class RegistrationView(APIView):

    def post(self, request, format=None):
        data = request.data
        trader = Trader.objects.filter(email=data[u'email'])
        if trader.exists():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        data[u'created_at'], data[u'updated_at'] = datetime.now(), ''
        serializer = TraderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class TradersView(APIView):

    def get(self, request, format=None):
        traders = Trader.objects.all()
        serializer = TraderSerializer(traders)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TraderSearchView(APIView):

    def delete(self, request):
        email = self.request.query_params.get('email', None)
        trader = Trader.objects.filter(email=email)
        if not trader.exists():
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        trader.delete()

        return Response({}, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        email = self.request.query_params.get('email', None)
        trader = Trader.objects.filter(email=email)
        serializer = TraderSerializer(trader, many=True)

        return Response(serializer.data[0], status=status.HTTP_200_OK)

    def put(self, request, format=None):
        trader = Trader.objects.filter(email=self.request.data.get('email', None))
        new_name = request.data.get('name', None)
        new_update_date = datetime.now()
        trader.update(name=new_name)

        return Response({}, status=status.HTTP_200_OK)


class TraderIDView(APIView):

    def get(self, request, trader_id):
        trader = Trader.objects.filter(id=trader_id)
        if not trader.exists():
            return Response("", status=status.HTTP_404_NOT_FOUND)

        serializer = TraderSerializer(trader, many=True)

        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, trader_id):
        trader = Trader.objects.filter(id=trader_id)
        if not trader.exists():
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        trader.delete()

        return Response({}, status=status.HTTP_200_OK)


class TraderTransaction(APIView):

    def put(self, request, format=None):
        trader = Trader.objects.filter(email=self.request.data.get('email', None))
        if not trader.exists():
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        new_balance = trader.first().balance + request.data.get('amount', None)
        new_update_date = datetime.now()
        trader.update(balance=new_balance)

        return Response({}, status=status.HTTP_200_OK)


class StocksDataView(APIView):

    def get(self, request, format=None):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StocksSymbolView(APIView):

    def get(self, request, symbol):
        stock = Stock.objects.filter(symbol=symbol)
        if not stock.exists():
            return Response("", status=status.HTTP_404_NOT_FOUND)

        serializer = StockSerializer(stock, many=True)

        return Response({}, status=status.HTTP_200_OK)