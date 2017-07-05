from django.conf.urls import url
from ttsx_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_check/$', views.register_check),
    url(r'^login/$', views.login),
]