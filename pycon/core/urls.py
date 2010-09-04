from django.conf.urls.defaults import *

urlpatterns = patterns('pycon.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^register/$', 'register', name='register'),
    url(r'^confirm/(?P<code>[\w\-]{27}\=)$', 'confirm', name='confirm'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^cfpsubmit/$', 'cfpsubmission', name='cfpsubmission'),
    url(r'^freeparticipantapply/$', 'freeparticipantapply', name='freeparticipantapply'),
    
)

urlpatterns += patterns('',
   url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html',}),
   url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                        )