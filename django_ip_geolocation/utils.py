from django_ip_geolocation import settings
from django.utils.module_loading import import_string
import logging

def get_remote_ip_from_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geolocation_backend_cls():
    geolocation_backend_cls = import_string(settings.IP_GEOLOCATION_SETTINGS.get('BACKEND'))
    return geolocation_backend_cls


def set_cookie(response, geolocation_data):
  response.set_cookie('geolocation', geolocation_data)
