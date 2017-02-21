from .. models import  Promise
from .. constants import *

class APILib(object):

	def __init__(self):
		pass

	def getPromiseStatus(self,reqObj):
		promises = Promise.objects.all()
		total = promises.count()
		completed = promises.filter(status = 'Completed').count()
		in_progress = promises.filter(status = 'In Progress').count()
		broken = promises.filter(status = 'Broken').count()
		not_started = promises.filter(status = 'Not Started').count()	
		return {'total':total,'completed':completed,'in_progress':in_progress,'broken':broken,'not_started':not_started}