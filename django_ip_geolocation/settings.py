from django.conf import settings

IP_GEOLOCATION_SETTINGS = {
    'BACKEND': 'django_ip_geolocation.backends.IPGeolocationAPI',
    'BACKEND_API_KEY': '',
    'BACKEND_USERNAME': '',
    'RESPONSE_HEADER': 'X-IP-Geolocation',
    'ENABLE_REQUEST_HOOK': True,
    'ENABLE_RESPONSE_HOOK': True,
    'ENABLE_COOKIE': False,
}

CUSTOM_IP_GEOLOCATION_SETTINGS = getattr(settings, 'IP_GEOLOCATION_SETTINGS', {})

IP_GEOLOCATION_SETTINGS.update(CUSTOM_IP_GEOLOCATION_SETTINGS)
