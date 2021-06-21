from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .mainPage import *
from .productPage import *
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