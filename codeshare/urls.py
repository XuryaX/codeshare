from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^snips/', include('snips.urls.snippets')),
    url(r'^lang/', include('snips.urls.languages')),
    url(r'', include('codeshare.acc.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', 'snips.views.snipviews.create_snippet'),
)
