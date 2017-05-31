from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.wish, name = 'wish'),
	url(r'^create$', views.create, name = 'create'),
	url(r'^add$', views.add, name = 'add'),
	url(r'^/item/(?P<id>\d+)', views.item, name = 'item'),
	url(r'^/copy/(?P<id>\d+)/(?P<user>\w+)', views.copy, name = 'copy'),
	url(r'^/delete/(?P<id>\d+)', views.delete, name = 'delete'),
	url(r'^/remove/(?P<id>\d+)/(?P<add>\w+)', views.remove, name = 'remove'),
]
