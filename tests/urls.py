#import django
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^test_geolocation/$', views.geolocation_test)
]
