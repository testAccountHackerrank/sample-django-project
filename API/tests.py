# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import connection
from django.test import TestCase
from rest_framework.test import RequestsClient
import json
from dateutil.parser import parse
from os import system
from .models import Stock
from DBDump import *


class RestTestCase(TestCase):

    def setUp(self):
        load_data_in_db()

        self.test_1 = []
        self.test_2 = []
        self.test_3 = []
        self.test_4 = []
        self.test_5 = []
        with open('TestData/http00.json') as f:
            for line in f:
                self.test_1.append(line)
        with open('TestData/http01.json') as f:
            for line in f:
                self.test_2.append(line)
        self.test_2 = self.test_1 + self.test_2
        with open('TestData/http02.json') as f:
            for line in f:
                self.test_3.append(line)
        self.test_3 = self.test_2 + self.test_3
        with open('TestData/http03.json') as f:
            for line in f:
                self.test_4.append(line)
        self.test_4 = self.test_3 + self.test_4
        with open('TestData/http04.json') as f:
            for line in f:
                self.test_5.append(line)
        self.test_5 = self.test_4 + self.test_5

    def test_set_1(self):
        client = RequestsClient()
        for ro in self.test_1:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            response = json.loads(res.text)
            self.assertEqual(response, row['response']['body'])

    def test_set_2(self):
        client = RequestsClient()
        for ro in self.test_2:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            response = json.loads(res.text)
            self.assertEqual(response, row['response']['body'])

    def test_set_3(self):
        client = RequestsClient()
        for ro in self.test_3:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            response = json.loads(res.text)
            self.assertEqual(response, row['response']['body'])

    def test_set_4(self):
        client = RequestsClient()
        for ro in self.test_4:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            response = json.loads(res.text)
            self.assertEqual(response, row['response']['body'])

    def test_set_5(self):
        client = RequestsClient()
        for ro in self.test_5:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'])
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'], json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            response = json.loads(res.text)
            self.assertEqual(response, row['response']['body'])