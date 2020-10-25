from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from .views import(
	StatusListAPIView,
	StatusCreateAPIView,
	StatusDetailAPIView,
	StatusUpdateAPIView,
	StatusDeleteAPIView,
	StatusMixinsAPIView
)


urlpatterns = [
	url(r'^$',StatusMixinsAPIView.as_view()),
	url(r'^create/$',StatusCreateAPIView.as_view()),
	url(r'^(?P<id>\d+)/$',StatusDetailAPIView.as_view()),
	url(r'^(?P<pk>\d+)/update/$',StatusUpdateAPIView.as_view()),
	url(r'^(?P<pk>\d+)/delete/$',StatusDeleteAPIView.as_view()),
]



#api view

#/api/status -> LIST API VIEW
#/api/status/create/ -> Create
#/api/status/1/ -> Detail
#/api/status/1/update -> Update
#/api/status/1/delete -> delete
