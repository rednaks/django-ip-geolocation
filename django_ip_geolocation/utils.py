"""Helper functions."""
import base64
import json
import logging
from django.utils.module_loading import import_string  # noqa: E501 # pylint: disable=import-error
from django_ip_geolocation import settings


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
    backend_path = settings.IP_GEOLOCATION_SETTINGS.get('BACKEND')
    geolocation_backend_cls = import_string(backend_path)
    return geolocation_backend_cls


def get_geolocation(request):
    """Fetch geolocation data.

    :param request: Django hooked request
    :type: django.http.HttpRequest
    :return: Geolocation data
    :rtype: dict
    """
    ip_addr = settings.IP_GEOLOCATION_SETTINGS.get('FORCE_IP_ADDR', None)
    if not ip_addr:
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
    encoded_data = base64.b64encode(
        json.dumps(geolocation_data).encode('utf-8'))
    response.set_cookie('geolocation', encoded_data)


def clean_geolocation_data(geolocation_data, attr_to_remove=None):
    """Remove attributes from geolocation data.

    If no attributes are provided, return a copy of the same data.

    :param geolocation_data: Full geolocation data
    :type: dict
    :param attr_to_remove: List of attributes to remove
    :type: list
    :return: Geolocation data (cleaned or copy)
    :rtype: dict
    """
    geolocation_copy = geolocation_data.copy()

    if attr_to_remove is None:
        return geolocation_copy

    for attr in attr_to_remove:
        try:
            del geolocation_copy[attr]
        except KeyError:
            logging.info('Key not found, continuing ...')

    return geolocation_copy


def is_user_consented(request):
    """Check if the user gave consent to be geolocatted.

    :param request: User http request
    :type: HttpRequest
    :return: Yes or no
    :rtype: bool
    """
    validator_path = settings.IP_GEOLOCATION_SETTINGS.get(
        'USER_CONSENT_VALIDATOR')
    user_consent_validator = None
    if validator_path is None:
        return True

    user_consent_validator = import_string(validator_path)
    return user_consent_validator(request)
