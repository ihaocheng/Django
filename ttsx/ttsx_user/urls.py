from django.conf.urls import url
from ttsx_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_check/$', views.register_check),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^user_center_info/', views.user_center_info),
]