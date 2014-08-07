from django.conf.urls import patterns,url


urlpatterns = patterns('',
                       url(r'^get/(?P<object_id>\d+)/$', 'snips.views.snipviews.snip_detail'),
                       url(r'', 'snips.views.snipviews.snipall'),



)