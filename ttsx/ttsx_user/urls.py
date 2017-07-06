from django.conf.urls import url
from ttsx_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_check/$', views.register_check),
    url(r'^register_check2/$', views.register_check2),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^login_check2/$', views.login_check2),
    url(r'^center_info/', views.center_info),
]