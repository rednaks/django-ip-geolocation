"""Default settings for the module."""
from django.conf import settings  # noqa: E501 # pylint: disable=import-error

IP_GEOLOCATION_SETTINGS = {
    'BACKEND': 'django_ip_geolocation.backends.IPGeolocationAPI',
    'BACKEND_API_KEY': '',
    'BACKEND_EXTRA_PARAMS': {},
    'BACKEND_USERNAME': '',
    'RESPONSE_HEADER': 'X-IP-Geolocation',
    'ENABLE_REQUEST_HOOK': True,
    'ENABLE_RESPONSE_HOOK': True,
    'ENABLE_COOKIE': False,
}

CUSTOM_IP_GEOLOCATION_SETTINGS = getattr(settings, 'IP_GEOLOCATION_SETTINGS', {})  # noqa: E501

IP_GEOLOCATION_SETTINGS.update(CUSTOM_IP_GEOLOCATION_SETTINGS)
