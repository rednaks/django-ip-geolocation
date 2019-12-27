from django.conf import settings
from django.utils.module_loading import import_string

def get_remote_ip_from_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geolocation_backend_cls():
    geolocation_backend = settings.GEOLOCATION_BACKEND
    if not geolocation_backend:
        geolocation_backend = 'django_ip_geolocation.backends.IPGeolocationAPI'
    
    geolocation_backend_cls = import_string(geolocation_backend)

    return geolocation_backend_cls

