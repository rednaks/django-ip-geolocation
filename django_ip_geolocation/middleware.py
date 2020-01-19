import logging

from django.utils.deprecation import MiddlewareMixin # pylint: disable=import-error
from django_ip_geolocation.utils import get_geolocation, set_cookie
from django_ip_geolocation import settings


class IpGeolocationMiddleware(MiddlewareMixin):
    "Mixin Middleware Hook"

    def __init__(self, get_response=None):
        self._geolocation_data = None
        super(IpGeolocationMiddleware).__init__(get_response)

    def process_request(self, request):
        "A hook on the request"

        try:
            if not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK'):
                return

            self._get_geolocation(request)
            request.geolocation = self._get_geolocation_data
        except Exception:
            logging.error("Couldn't geolocate ip", exc_info=True)

    def process_response(self, request, response):
        "A hook on the response"

        try:
            if not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_RESPONSE_HOOK') and \
                    not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_COOKIE'):
                return response

            if self._geolocation_data is None:
                self._get_geolocation(request)

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK'):
                # Response hook is enabled
                header = settings.IP_GEOLOCATION_SETTINGS.get('RESPONSE_HEADER')
                response[header] = self._geolocation_data

            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_COOKIE'):
                set_cookie(response, self._geolocation_data)

        except Exception:
            logging.error("Couldn't geolocate ip", exc_info=True)

        return response

    def _get_geolocation(self, request):
        "Helper internal method to fetch geolcation using backend defined in settings"
        self._geolocation_data = get_geolocation(request)
