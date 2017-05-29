from django.conf.urls import patterns, url, include
from .views import DressList


urlpatterns = patterns('',
                url(r'^dresses/', DressList.as_view(), name='api-dresses-list'),
)
