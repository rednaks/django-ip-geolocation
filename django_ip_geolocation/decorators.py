"""Django view decorator."""

import logging
from django_ip_geolocation.utils import get_geolocation, set_cookie, \
    clean_geolocation_data
from django_ip_geolocation.settings import IP_GEOLOCATION_SETTINGS as _settings


def with_ip_geolocation(view_func):
    """Decorate a django view, to add geolocation data to request/response.

    :param: view_func: Django view function
    :type: function
    :return: A wrapper function
    :rtype: function
    """
    def inner(request):  # noqa: E501
        try:
            enable_request = _settings.get('ENABLE_REQUEST_HOOK')
            enable_response = _settings.get('ENABLE_RESPONSE_HOOK')
            enable_cookie = _settings.get('ENABLE_COOKIE', False)

            if not enable_request and not (enable_response or enable_cookie):
                return view_func(request)

            geolocation = get_geolocation(request)

            if enable_request:
                request.geolocation = geolocation

            response = view_func(request)

            if enable_response:
                header = _settings.get('RESPONSE_HEADER')
                response[header] = geolocation

            if enable_cookie:
                cleaned_geolocation_data = clean_geolocation_data(
                    geolocation, ['raw_data'])
                set_cookie(response, cleaned_geolocation_data)

            return response
        except Exception:
            logging.error('Django Ip Geolocation Error', exc_info=True)
            return view_func(request)

    return inner
