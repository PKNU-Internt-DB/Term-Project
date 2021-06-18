from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.parsers import JSONParser

from .models import *


def getCustomer(request):
    if request.method == 'GET':
        # data = JSONParser().parse(request)
        # customer_id = data['Customer_id']

        customer_id = 2.0
        query_orders = Orders.objects.filter(customer=customer_id)

        for q_o in query_orders:
            print(q_o.order_id)

            # query_items = OrderItems.objects.filter(order=q_o.order_id)
            # for q_i in query_items:
            #     print(q_i.unit_price)

        # for q_o in query_orders:
        #     print(OrderItems.objects.filter(order_id=q_o('order_id'))

        return JsonResponse(
            {
                'message': 'Customer test message',
            }
        )


def getRecord(request):
    if request.method == 'GET':
        # data = JSONParser().parse(request)
        # employees_id = data['Employee_id']
        # orders = Orders.objects.filter(salesman=54.0)

        # order_id = []
        # for o in orders:
        #     print(o)
        #     order_id.append(o)

        # sum = 0
        # for o_i in order_id:
        #     print(OrderItems.objects.filter(order=o_i))
        #     # sum = OrderItems.objects.get(order=o_i)
        #     # print(sum)
        return JsonResponse(
            {
                'message': 'Record test message',
            }
        )
