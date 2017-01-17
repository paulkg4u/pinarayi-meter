from django.shortcuts import render
from django.http import  HttpResponse

from libs.promiseLib import  PromiseLib

from helpers import  Collection

# Create your views here.
def index(request):
    promiseLib = PromiseLib()
    topPromises = promiseLib.get_top_promises()
    # promises = promiseLib.list_promise()
    response = {'topPromises':topPromises}
    # response['promises'] = promises
    return render(request,'pinarayi_meter/index.html',response)

def promise(request, uuid):
    reqObj = Collection()
    reqObj.uuid = uuid

    promiseLib =PromiseLib()
    promiseDetails = promiseLib.get_promise(reqObj)
    response = {'promiseDetails':promiseDetails}
    return render(request,'pinarayi_meter/promise.html',response)

