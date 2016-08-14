from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from oauth.views import *

urlpatterns = [
	url(r'^$', home),
	url(r'', include('social.apps.django_app.urls', namespace='social')),
	# url(r'^login/$', ulogin),
	url('', include('django.contrib.auth.urls',namespace='auth')),
]