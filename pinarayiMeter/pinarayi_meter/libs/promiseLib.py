from .. models import  Promise

class PromiseLib(object):
    def __init__(self):
        pass

    def list_promise(self):
        promises = Promise.objects.all()
        return  promises

    def get_promise(self,reqObj):
        promise = Promise.objects.get(uuid = reqObj.uuid)
        return  promise

    def get_promise_by_category(self,reqObj):
        pass

    def get_promise_by_status(self,reqObj):
        pass