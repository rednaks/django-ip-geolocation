from django_ip_geolocation.utils import get_remote_ip_from_request, get_geolocation_backend_cls
from django_ip_geolocation import settings
import logging


def with_ip_geolocation(view_func):

    def inner(request):
        try:
            if not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK') and \
                    not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_RESPONSE_HOOK'):
                return view_func(request)

            ip = get_remote_ip_from_request(request)
            backend_cls = get_geolocation_backend_cls()
            backend_instance = backend_cls(ip)
            geolocation = backend_instance.geolocate()

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK'):
                request.geolocation = geolocation

            response = view_func(request)

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_RESPONSE_HOOK'):
                response[settings.IP_GEOLOCATION_SETTINGS.get('RESPONSE_HEADER')] = geolocation

            return response
        except Exception as e:
            logging.error('Django Ip Geolocation Error', exc_info=True)
            return view_func(request)

    return inner

