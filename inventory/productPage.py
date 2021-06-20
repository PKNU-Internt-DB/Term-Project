from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.parsers import JSONParser
import json

from .models import *

#   url /customer
#   http-method : GET
#   parameter : null
#   respone :
#           cusotmer_id : [puchase_count, price_sum]


def getCustomer(request):

    result_dict = dict()
    customer_id_set = Customers.objects.values('customer_id')

    for c_id_set in customer_id_set:
        order_set = Orders.objects.values(
            'order_id').filter(customer=c_id_set['customer_id'])

        price_sum = 0
        purchase_count = 0

        for o_set in order_set:
            price_set = OrderItems.objects.values(
                'unit_price').filter(order=o_set['order_id'])
            purchase_count += len(price_set)

            for p_set in price_set:
                price_sum += p_set['unit_price']

        result_dict[c_id_set['customer_id']] = [purchase_count, price_sum]

    json_result = json.dumps(result_dict)
    return json_result


#   url /customer/[customer_id]
#   http-method : GET
#   parameter : null
#   respone :
#           id : customer_id
#           product : [product_count, list_price]
def getCustomerDetail(request, customer_id):

    result_dict = dict()
    result_dict['id'] = customer_id

    order_set = Orders.objects.values(
        'order_id').filter(customer=customer_id)

    for o_set in order_set:
        order_item_set = OrderItems.objects.values(
            'product').filter(order=o_set['order_id'])

        for o_i_set in order_item_set:
            product_name = Products.objects.values(
                'product_name').get(product_id=o_i_set['product'])['product_name']
            product_list_price = Products.objects.values(
                'list_price').get(product_id=o_i_set['product'])['list_price']

            if product_name in result_dict:
                count = result_dict.get(product_name)[0]
                result_dict[product_name] = [count+1, product_list_price]
            else:
                result_dict[product_name] = [1, product_list_price]

    json_result = json.dumps(result_dict)
    return json_result


#   url /record
#   http-method : GET
#   parameter : null
#   respone :
#           employee_name : [employee_id, price_sum]
def getRecord(request):

    result_dict = dict()
    salesman_set = Employees.objects.values(
        'employee_id').filter(job_title__contains='Sales')

    for s_set in salesman_set:
        order_set = Orders.objects.values('order_id').filter(
            salesman=s_set['employee_id'])

        employee_first_name = Employees.objects.values(
            'first_name').get(employee_id=s_set['employee_id']).get('first_name')
        employee_last_name = Employees.objects.values(
            'last_name').get(employee_id=s_set['employee_id']).get('last_name')

        price_sum = 0
        for o_set in order_set:
            item_set = OrderItems.objects.values(
                'unit_price').filter(order_id=o_set['order_id'])

            for i_set in item_set:
                price_sum += i_set['unit_price']

        if price_sum != 0:
            result_dict[employee_first_name + ' ' +
                        employee_last_name] = [s_set['employee_id'], price_sum]

    json_result = json.dumps(result_dict)
    return json_result
