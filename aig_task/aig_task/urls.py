from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'general.views.home', name='home'),
    url(r'^(?P<ref_id>.*)$', 'general.views.words', name='words'),
]
