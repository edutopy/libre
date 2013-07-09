from django.conf.urls.defaults import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (SourceDataVersionList, SourceDataVersionDetail, SourceList, SourceDetail,
    SourceGetAll, SourceGetOne)

urlpatterns = patterns('data_drivers.views',
    url(r'^$', 'api_root', name='api_root'),
    url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^sources/$', SourceList.as_view(), name='source-list'),
    url(r'^sources/(?P<slug>[-\w]+)/$', SourceDetail.as_view(), name='source-detail'),
    url(r'^sources/(?P<slug>[-\w]+)/data/$', SourceGetAll.as_view(), name='source-get_all'),
    url(r'^sources/(?P<slug>[-\w]+)/data/(?P<id>[0-9]+)/$', SourceGetOne.as_view(), name='source-get_one'),

    url(r'^sources/data_version/$', SourceDataVersionList.as_view(), name='sourcedataversion-list'),
    url(r'^sources/data_versions/(?P<pk>[0-9]+)/$', SourceDataVersionDetail.as_view(), name='sourcedataversion-detail'),

)

urlpatterns = format_suffix_patterns(urlpatterns)
