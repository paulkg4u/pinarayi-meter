from django.shortcuts import render
from django.http import  HttpResponse

from libs.promiseLib import  PromiseLib

from constants import  Collection
# Create your views here.
def index(request):
    promiseLib = PromiseLib()
    result = promiseLib.list_promise()
    return HttpResponse("hello malayali")

def promise(request, uuid):
    reqObj = Collection()
    reqObj.uuid = uuid
    promiseLib =PromiseLib()
    result = promiseLib.get_promise(reqObj)
    return HttpResponse("list promise")

