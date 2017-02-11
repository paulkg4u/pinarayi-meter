from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home$',views.index,name = "index"),
    url(r'^details/(?P<uuid>[\w\-]+)$',views.promise,name = "promise"),
	url(r'^api/status',views.statusApi, name ="statusApi"),
	url(r'^api/category',views.categoryApi,name = "categoryApi")
]