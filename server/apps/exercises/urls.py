from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from apps.exercises import views

urlpatterns = patterns('',
                       url(r'^/fetch/(?P<tag>[^/]*)/(?P<qid>[0-9]*)/?$',
                           views.fetch_ex, name='fetch'),
                       url(r'^/attempt/(?P<attempt>[^/]*)/(?P<correct>[01])/?$', 
                           views.set_attempt, name='attempt'),
                       #url(r'^/build/?$', views.build, name='build'),
                       url(r'^/edit/?$', views.edit, name='edit'),
                      )
