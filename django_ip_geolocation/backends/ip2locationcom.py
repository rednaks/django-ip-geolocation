"""IP2location.com service integration."""

import requests
from django_ip_geolocation.backends import GeolocationBackend
from django_ip_geolocation.settings import IP_GEOLOCATION_SETTINGS as _settings


class IP2LocationCom(GeolocationBackend):
    """IP2location.com backend implementation."""

    def geolocate(self):
        """Call ip2location.com api."""
        api_key = _settings.get('BACKEND_API_KEY')
        extra_params = _settings.get('BACKEND_EXTRA_PARAMS', {})

        if not api_key:
            msg = "BACKEND_API_KEY is required. Please provide an API_KEY in IP_GEOLOCATION_SETTINGS"  # noqa: E501
            raise Exception(msg)

        payload = {
            'key': api_key,
            'ip': self._ip,
            'package': extra_params.get('package', 'WS24')
        }

        url = 'https://api.ip2location.com/v2/'
        res = requests.get(url, params=payload)
        if res.ok:
            self._raw_data = res.json()
        else:
            raise Exception(res.text)

    def _parse(self):
        """Parse raw data."""
        self._continent = self._raw_data.get('continent_name')
        self._country = {
            'code': self._raw_data.get('country_code'),
            'name': self._raw_data.get('country_name'),
        }

        self._geo_data = {
            'latitude': self._raw_data.get('latitude'),
            'longitude': self._raw_data.get('longitude'),
        }
