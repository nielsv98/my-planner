from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^events/$', views.event_overview, name='event_overview'),
    url(r'^events/new/$', views.event_new, name='event_new'),
    url(r'^events/edit/$', views.event_edit, name='event_edit'),
    url(r'^register/$', views.register_view, name='register_view')
]
