from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='login_view'),
    url(r'^register/$', views.register_view, name='register_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^events/$', views.event_overview, name='event_overview'),
    url(r'^events/new/$', views.event_new, name='event_new'),
    url(r'^events/list/$', views.event_list, name='event_list'),
    url(r'^events/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^events/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^events/(?P<pk>\d+)/delete/$', views.event_delete, name='event_delete'),
    url(r'^lists/$', views.ApiList.as_view()),
    url(r'^lists/(?P<pk>\d+)/$', views.ApiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
