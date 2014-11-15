from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'baseapp.views.index', name = 'name'),
    url(r'^adduser/$', 'baseapp.views.AddUser', name = 'cool'),
    url(r'^addevent/$', 'baseapp.views.AddEvent', name ='uncool'), 
    url(r'^admin/', include(admin.site.urls)),
)
