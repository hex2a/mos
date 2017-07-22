from django.conf.urls import patterns


urlpatterns = patterns('',
    (r'^$', 'announce.views.announce'),
)
