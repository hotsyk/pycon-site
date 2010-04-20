from django.conf.urls.defaults import *

urlpatterns = patterns('pycon.core.views',
    url(r'^$', 'index', name='index'),
)
