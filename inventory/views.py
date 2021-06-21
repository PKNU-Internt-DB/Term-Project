from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .mainPage import *
from .productPage import *
from .loginPage import *
@csrf_exempt
def mainPage1(request):
    if request.method == 'GET':
        return JsonResponse(getMain1(),safe=False)
def mainPage3(request):
    if request.method=='GET':
        return JsonResponse(getMain3(request.GET.get('ware_id')),safe=False)
@csrf_exempt
def productPage(request):
    if request.method=='GET':
        return JsonResponse(getProduct(),safe=False)



@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        return postLogin(request)



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
