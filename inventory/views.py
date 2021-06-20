from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .mainPage import getMain
from .productPage import *
from .loginPage import *


@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        return postLogin(request)


@csrf_exempt
def mainPage(request):
    if request.method == 'GET':
        return getMain()


@csrf_exempt
def customerPage(request):
    if request.method == 'GET':
        return JsonResponse(getCustomer(request), safe=False)


@csrf_exempt
def customerDetailPage(request, customer_id):
    if request.method == 'GET':
        return JsonResponse(getCustomerDetail(request, customer_id), safe=False)


@csrf_exempt
def recordPage(request):
    if request.method == 'GET':
        return JsonResponse(getRecord(request), safe=False)


# @csrf_exempt
# def recordCountryPage(request):
#     if request.method == 'GET':
#         return JsonResponse(getRecordCountry(request), safe=False)
