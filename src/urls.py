from django.conf.urls.defaults import *
from sample.flows import SampleFlow

urlpatterns = patterns('',
    url(r'^flow/', include(SampleFlow().urls), name="flow"),
)
