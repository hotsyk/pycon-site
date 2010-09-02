from django.conf.urls.defaults import *

urlpatterns = patterns('pycon.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^register/$', 'register', name='register'),
    url(r'^confirm/(?P<code>[\w\-]{27}\=)$', 'confirm', name='confirm'),
)
