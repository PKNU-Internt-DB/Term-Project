from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .mainPage import getMain
from .productpage import getProduct
@csrf_exempt
def mainPage(request):
    if request.method == 'GET':
        return getMain()

@csrf_exempt
def productPage(request):
    if request.method=='GET':
        return getProduct()