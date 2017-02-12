from django.shortcuts import render
from django.http import  HttpResponse
from django.http import  JsonResponse
from libs.promiseLib import  PromiseLib, CategoryLib
from libs.statusLib import StatusLib

from helpers import  Collection



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
    statusLib = StatusLib()
    response = statusLib.getPromiseStatus(reqObj)
    return JsonResponse(response)

def categoryApi(request):
    reqObj = Collection()
    reqObj.categoryList = request.GET.dict()['categoryList']
    reqObj.type = request.GET.dict()['type']
    categoryLib = CategoryLib()
    response = categoryLib.get_promise_by_category(reqObj)
    return JsonResponse(response)


