from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, about
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^about', about),
    # url(r'^admin/', include(admin.site.urls)),
)
