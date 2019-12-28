from django.conf import settings
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
    geolocation_backend = 'django_ip_geolocation.backends.IPGeolocationAPI'
    try:
        geolocation_backend = settings.GEOLOCATION_BACKEND
    except Exception:
        logging.warning('Using default logger %s', geolocation_backend, exc_info=True)

    
    geolocation_backend_cls = import_string(geolocation_backend)

    return geolocation_backend_cls

