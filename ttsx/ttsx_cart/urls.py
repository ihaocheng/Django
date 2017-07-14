from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^place_order/$', views.place_order),

]