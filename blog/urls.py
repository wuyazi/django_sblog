from django.conf.urls import patterns, include, url
from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.foo.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'sblog.views.blog_list', name='home'),

    url(r'^500$','sblog.views.errorpage',name='errorpage'),

    url(r'^register$','sblog.views.register',name='register'),
    url(r'^login$','sblog.views.login',name='login'),
    url(r'^logout$','sblog.views.logout',name='logout'),

    url(r'^user/(?P<id>\d+)/$','sblog.views.user',name='user'),
    url(r'^search$','sblog.views.blog_search',name='search'),

    #url(r'^sblog/', include('sblog.urls')),
    url(r'^newblog/$', 'sblog.views.blog_list', name='bloglist'),
    url(r'^tag/(?P<id>\d+)/$', 'sblog.views.blog_filter', name='filtrblog'),
    url(r'^blog/(?P<id>\d+)/$', 'sblog.views.blog_show', name='detailblog'),
    url(r'^blog/add/$', 'sblog.views.blog_add', name='addblog'),
    url(r'^comment/add/$', 'sblog.views.comment_add', name='addcomment'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(os.path.dirname(__file__), '../static').replace('\\','/')}),
)
