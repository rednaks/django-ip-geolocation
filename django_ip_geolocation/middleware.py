from django.utils.deprecation import MiddlewareMixin
from django_ip_geolocation.utils import get_remote_ip_from_request, get_geolocation_backend_cls
from django_ip_geolocation import settings

class IpGeolocationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK'):
            return
        request.geolocation = self._get_geolocation(request)

    def process_response(self, request, response):

        if not settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_RESPONSE_HOOK'):
            return response

        header = settings.IP_GEOLOCATION_SETTINGS.get('RESPONSE_HEADER')
        if not hasattr(request, 'geolocation'):
            if settings.IP_GEOLOCATION_SETTINGS.get('ENABLE_REQUEST_HOOK'):
                return response
            else:
                # Response hook is enabled
                response[header] = self._get_geolocation(request)
                return response

        response[header] = getattr(request, 'geolocation')
        return response

    def _get_geolocation(self, request):
        ip = get_remote_ip_from_request(request)
        backend_cls = get_geolocation_backend_cls()
        backend_instance = backend_cls(ip)
        geolocation = backend_instance.geolocate()
        return geolocation


