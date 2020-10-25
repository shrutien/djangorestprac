from django.urls import path
from .views import login_page,home,dashboard,register
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
	url(r'^$', login_page, name='login_page'),
	url(r'^api/', include('catalog.api.urls')),
	url(r'^home/$', home, name='home'),
	url(r'^dashboard/$', dashboard, name='dashboard'),
	url(r'^register/$', register, name='register'),
]