from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, about, location, campaign, lists
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^about', about),
    url(r'^lists', lists),
    url(r'^$', home),
    url(r'^about', about),
    url(r'^location', location),
    url(r'^campaign/(?P<question_id>\d+)/$', campaign, name="campaign"),
    # url(r'^admin/', include(admin.site.urls)),
)
