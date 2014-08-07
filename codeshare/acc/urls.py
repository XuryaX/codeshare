from django.conf.urls import patterns,url


urlpatterns = patterns('',
                       url(r'^login/$', 'codeshare.acc.views.login'),
                       url(r'^signup/$', 'codeshare.acc.views.signup'),
                       url(r'^logout/$', 'codeshare.acc.views.logout'),

)