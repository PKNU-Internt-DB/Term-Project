from .models import *
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.parsers import JSONParser
import json

def getProduct():
    product=Products.objects.values('product_name','list_price','category','description')
    tmp_list = []
    for p in product:
        category_name = ProductCategories.objects.filter(category_id=p['category']).values('category_name')

        tmp_dict = dict()
        tmp_dict['product_name'] = p['product_name']
        tmp_dict['list_price'] = p['list_price']
        tmp_dict['category'] = category_name[0]['category_name']
        tmp_dict['description'] = p['description']

        tmp_list.append(tmp_dict)

    # print(tmp_list)
    obj1=json.dumps(tmp_list,indent="\t")
    print(obj1)
    return obj1


#   url /customer
#   http-method : GET
#   parameter : null
#   respone :
#           {
#           cusotmer_id : cusotmer_id,
#           puchase_count : puchase_count,
#           price_sum : price_sum,
#           }


def getCustomer(request):

    result_list = []
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

        result_dict = dict()
        result_dict["customer_id"] = c_id_set['customer_id']
        result_dict["purchase_count"] = purchase_count
        result_dict["price_sum"] = price_sum

        result_list.append(result_dict)

    json_result = json.dumps(result_list, indent="\t")
    return json_result


#   url /customer/[customer_id]
#   http-method : GET
#   parameter : null
#   respone :
#           id : customer_id
#           product_name : {
#               product_name : product_name
#               product_count : product_count
#               list_price : list_price
#           }

def getCustomerDetail(request, customer_id):

    result_list = []
    # result_dict['customer_id'] = customer_id

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

            tmp_dict = dict()
            tmp_dict['product_name'] = product_name
            tmp_dict['purchase_count'] = 1
            tmp_dict['product_list_price'] = product_list_price

            result_list.append(tmp_dict)

    json_result = json.dumps(result_list, indent="\t")
    print(json_result)
    return json_result


#   url /record
#   http-method : GET
#   parameter : null
#   respone :
#           {
#           employee_id : employee_id,
#           employee_name : employee_name,
#           price_sum : price_sum,
#           }
def getRecord(request):

    result_list = []
    salesman_set = Employees.objects.values(
        'employee_id').filter(job_title__contains='Sales')

    for s_set in salesman_set:
        order_set = Orders.objects.values('order_id').filter(
            salesman=s_set['employee_id'])

        employee_name = Employees.objects.values(
            'last_name').get(employee_id=s_set['employee_id']).get('last_name') + ' ' + Employees.objects.values(
            'first_name').get(employee_id=s_set['employee_id']).get('first_name')

        price_sum = 0
        for o_set in order_set:
            item_set = OrderItems.objects.values(
                'unit_price').filter(order_id=o_set['order_id'])

            for i_set in item_set:
                price_sum += i_set['unit_price']

        result_dict = dict()
        result_dict["employee_id"] = s_set['employee_id']
        result_dict["employee_name"] = employee_name
        result_dict["price_sum"] = price_sum

        result_list.append(result_dict)

    json_result = json.dumps(result_list, indent="\t")
    print(json_result)
    return json_result
