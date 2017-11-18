from django.conf.urls import url

from appoit import views

urlpatterns = [
    url(r'^(?P<time_id>\d+)/(?P<doctor_id>\d+)/(?P<time>\d+)/$', views.AppoitEngine),
    url(r'check/$', views.checkAppoit),
    url(r'validate/$', views.secret),
    url(r'^doctor/(?P<doctor_id>\d+)', views.doctor_Details),

]
