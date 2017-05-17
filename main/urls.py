from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name="home"),
    url(r'^team_member/(?P<id>[0-9+])', views.team_member_detail, name="team_member"),
    url(r'^contactform/$', views.contactform, name="contactForm"),
    url(r'^mail_success/$', views.mail_success.as_view(), name="mail_success"),
]
