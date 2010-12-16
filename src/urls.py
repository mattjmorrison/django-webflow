from django.conf.urls.defaults import *
from example.flows import SampleFlow, OtherFlow

urlpatterns = patterns('',
    url(r'^first/', include(SampleFlow().urls, namespace="first"), name="first"),
    url(r'^second/', include(OtherFlow().urls, namespace="second"), name="second"),
)
