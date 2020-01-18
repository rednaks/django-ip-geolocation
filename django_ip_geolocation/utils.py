from django_ip_geolocation import settings
from django.utils.module_loading import import_string # pylint: disable=import-error


def _get_remote_ip_from_request(request):
    """Retrieves remote ip addr from request

    :param request: Django request
    :type: django.http.HttpRequest
    :return: Ip address
    :rtype: str
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_addr = x_forwarded_for.split(',')[0]
    else:
        ip_addr = request.META.get('REMOTE_ADDR')
    return ip_addr


def _get_geolocation_backend_cls():
    """Retuns geolocation backend class

    :return: Geolocation backend class
    :rtype: class
    """

    geolocation_backend_cls = import_string(settings.IP_GEOLOCATION_SETTINGS.get('BACKEND'))
    return geolocation_backend_cls


def get_geolocation(request):
    """get_geolocation

    :param request: Django hooked request
    :type: django.http.HttpRequest
    :return: Geolocation data
    :rtype: dict
    """

    ip_addr = _get_remote_ip_from_request(request)
    backend_cls = _get_geolocation_backend_cls()
    backend_instance = backend_cls(ip_addr)

    return backend_instance.geolocate().data()


def set_cookie(response, geolocation_data):
    """Adds geolocation data in response cookie

    :param response:
    :type: django.http.HttpResponse
    :param geolocation_data: Geolocation data
    :type: dict
    :rtype: None
    """
    response.set_cookie('geolocation', geolocation_data)
