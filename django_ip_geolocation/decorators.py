from django_ip_geolocation.utils import get_remote_ip_from_request, get_geolocation_backend_cls


def with_ip_geolocation(view_func):

    def inner(request):
        try:
            ip = get_remote_ip_from_request(request)
            backend_cls = get_geolocation_backend_cls()
            backend_instance = backend_cls(ip)
            geolocation = backend_instance.geolocate()

            request.geolocation = geolocation
            response = view_func(request)
            response['X-GEOLOCATION'] = geolocation

            return response
        except Exception as e:
            pass

    return inner

