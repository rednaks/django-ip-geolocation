"""Helper functions."""
from django_ip_geolocation import settings
from django.utils.module_loading import import_string  # noqa: E501 # pylint: disable=import-error


def _get_remote_ip_from_request(request):
    """Retrieve remote ip addr from request.

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
    """Retun geolocation backend class.

    :return: Geolocation backend class
    :rtype: class
    """
    backend_class_name = settings.IP_GEOLOCATION_SETTINGS.get('BACKEND')
    geolocation_backend_cls = import_string(backend_class_name)
    return geolocation_backend_cls


def get_geolocation(request):
    """Fetch geolocation data.

    :param request: Django hooked request
    :type: django.http.HttpRequest
    :return: Geolocation data
    :rtype: dict
    """
    ip_addr = _get_remote_ip_from_request(request)
    backend_cls = _get_geolocation_backend_cls()
    backend_instance = backend_cls(ip_addr)

    backend_instance.geolocate()
    return backend_instance.data()


def set_cookie(response, geolocation_data):
    """Add geolocation data in response cookie.

    :param response:
    :type: django.http.HttpResponse
    :param geolocation_data: Geolocation data
    :type: dict
    :rtype: None
    """
    response.set_cookie('geolocation', geolocation_data)
