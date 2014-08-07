__author__ = 'Shaurya'

from django.conf.urls import patterns,url


urlpatterns = patterns('',
                       url(r'^get/(?P<slg>[-\w]+)/$', 'snips.views.lang.lang_detail'),
                       url(r'', 'snips.views.lang.lang_all'),

)