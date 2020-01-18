import logging
from django_ip_geolocation.utils import get_geolocation, set_cookie
from django_ip_geolocation import settings


def with_ip_geolocation(view_func):
    "decorator hook"

    def inner(request):
        try:
            if not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK') and \
                    not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_RESPONSE_HOOK'):
                return view_func(request)

            geolocation = get_geolocation(request)

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK'):
                request.geolocation = geolocation

            response = view_func(request)

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_RESPONSE_HOOK'):
                response[settings.IP_GEOLOCATION_SETTINGS.get('RESPONSE_HEADER')] = geolocation

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_COOKIE', False):
                set_cookie(response, geolocation)

            return response
        except Exception:
            logging.error('Django Ip Geolocation Error', exc_info=True)
            return view_func(request)

    return inner
