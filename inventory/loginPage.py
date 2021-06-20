from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from .models import *


def check(id, pw):
    check_id = Employees.objects.values('employee_id').get(
        employee_id=id)['employee_id']
    if str(id) == str(pw) and str(check_id) == str(id):
        return True
    return False


#   url /login
#   http-method : POST
#   parameter : id / pw
#   respone : login scusees / login fail
def postLogin(request):
    data = JSONParser().parse(request)
    id = data['user_id']
    pw = data['user_password']

    if check(id, pw):
        return JsonResponse({'code': '0000', 'msg': '로그인 성공'}, status=200)
    else:
        return JsonResponse({'code': '1001', 'msg': '로그인 실패'}, status=200)
