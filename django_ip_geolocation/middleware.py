from django.utils.deprecation import MiddlewareMixin
from django_ip_geolocation.utils import get_remote_ip_from_request, get_geolocation_backend_cls

class IpGeolocationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = get_remote_ip_from_request(request)
        request.geolocation = self._get_geolocation(ip)

    def process_response(self, request, response):
        if not hasattr(request, 'geolocation'):
            return response

        response['X-GEOLOCATION'] = getattr(request, 'geolocation')
        return response

    def _get_geolocation(self, ip):
        backend_cls = get_geolocation_backend_cls()
        backend_instance = backend_cls(ip)
        geolocation = backend_instance.geolocate()
        return geolocation


