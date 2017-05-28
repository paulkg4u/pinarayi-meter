from django.core import serializers

from .. models import  Promise, ReferenceObj
from .. constants import *


import json

class PromiseLib(object):
    def __init__(self):
        pass

    def list_promise(self):
        promises = Promise.objects.all()
        return  promises

    def get_top_promises(self):
        promises = Promise.objects.filter(category = THIRTY_FIVE_POINT_PROGRAMME)[:5]
        return promises
        
    def get_promise(self,reqObj):
        promise = Promise.objects.get(uuid = reqObj.uuid)
        return  promise

    def get_promise_by_category(self,reqObj):
        promises = Promise.objects.filter(category = reqObj.category)
        return promises

    def get_promise_by_status(self,reqObj):
        pass

    def get_promise_by_category_list(self,reqObj):

        reqObj.categoryList = CATEGORY_CONSTANTS[reqObj.category_name]['categories']
        promises = Promise.objects.filter(category__in =  reqObj.categoryList)
        return {'promises':promises,'category_name':CATEGORY_CONSTANTS[reqObj.category_name]['name']}

    def get_reference_objects(self, reqObj):
        referenceObjects = ReferenceObj.objects.filter(promise = reqObj, approved = True)
        return referenceObjects


class CategoryLib(object):
    def __init__(self):
        pass

    def get_promise_by_category(self,reqObj):
        promises = Promise.objects.filter(category__in = reqObj.categoryList)
        data = serializers.serialize('json', promises)
        return {'promises':json.loads(data)}


class RelatedObjectLib(object):
    def __init__(self):
        pass

    def add_related_object(self, reqObj):
        promiseObj = Promise.objects.get(uuid = reqObj.data['uuid'])
        newReference = ReferenceObj.objects.create(
                promise =promiseObj,
                referenceType = reqObj.data['type'],
                referenceLink = reqObj.data['link'],
                title = reqObj.data['title'],
                comments = reqObj.data['descr']
            )
        return {'status':True}
