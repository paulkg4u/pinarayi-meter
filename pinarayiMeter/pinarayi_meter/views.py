from django.shortcuts import render
from django.http import  HttpResponse
from django.http import  JsonResponse
from libs.promiseLib import  PromiseLib, CategoryLib
from libs.statusLib import APILib

from helpers import  Collection

import json

# Create your views here.
def index(request):
    promiseLib = PromiseLib()
    topPromises = promiseLib.get_top_promises()
    response = {'topPromises':topPromises,'status':{'name':'paul'}}
    return render(request,'pinarayi_meter/index.html',response)

def promise(request, uuid):
    reqObj = Collection()
    reqObj.uuid = uuid

    promiseLib =PromiseLib()
    promiseDetails = promiseLib.get_promise(reqObj)
    response = {'promiseDetails':promiseDetails}
    return render(request,'pinarayi_meter/promise.html',response)

def statusApi(request):
    reqObj = Collection()
    apiLib = APILib()
    response = apiLib.getPromiseStatus(reqObj)
    return JsonResponse(response)

def categoryApi(request):
    reqObj = Collection()
    reqObj.categoryList = request.GET.getlist('categoryList')
    reqObj.type = request.GET.dict()['type']
    categoryLib = CategoryLib()
    response = categoryLib.get_promise_by_category(reqObj)
    return JsonResponse(response)

def thirtFivePoint(request):
    reqObj = Collection()
    reqObj.category = 'Thirty Five Point Programme'
    promiseLib = PromiseLib()
    response = {}
    response['promises'] = promiseLib.get_promise_by_category(reqObj)
    return render(request, 'pinarayi_meter/thirty_five.html',response)

def category(request,category_name):
    reqObj = Collection()
    response = {}
    reqObj.category_name = category_name
    promiseLib = PromiseLib()
    response = promiseLib.get_promise_by_category_list(reqObj)
    
    return render(request, 'pinarayi_meter/category.html',response)

