from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.SocialCredentialList.as_view()),
    url(r'^read/$', views.SocialCredentialList.as_view()),
    url(r'^update/$', views.SocialCredentialDetail.as_view()),
    url(r'^delete/(?P<social_credential_id>[0-9]+)/$', views.SocialCredentialDetail.as_view()),
]
