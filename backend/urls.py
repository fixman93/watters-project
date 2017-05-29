from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site as filebrowser_site


urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('djoser.urls')),
    url(r'^api/v1/', include('apps.api.urls')),
)
