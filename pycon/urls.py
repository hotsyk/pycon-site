from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('pycon.core.urls')),

)

if settings.DEBUG:
    media_url = settings.MEDIA_URL
    if media_url.startswith('/'):
        media_url = media_url.strip('/')
    
    urlpatterns += patterns('django.views.static',
        (r'^%s/(?P<path>.*)$' % media_url, 'serve',
         {'document_root': settings.MEDIA_ROOT,
          'show_indexes': True}),
    )
        
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )        