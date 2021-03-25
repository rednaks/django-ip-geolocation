"""ipdata.co service integration."""
import requests
from django_ip_geolocation.backends import GeolocationBackend
from django_ip_geolocation import settings


class IPDataCo(GeolocationBackend):
    """ipdata.co backend implementation."""

    def geolocate(self):
        """Call ipdata api."""
        api_key = settings.IP_GEOLOCATION_SETTINGS.get('BACKEND_API_KEY')

        if not api_key:
            msg = "BACKEND_API_KEY is required. Please provide an API_KEY in IP_GEOLOCATION_SETTINGS"  # noqa: E501
            raise Exception(msg)

        payload = {'api-key': api_key}
        url = 'https://api.ipdata.co/{}'.format(self._ip)
        res = requests.get(url, params=payload)
        if res.ok:
            self._raw_data = res.json()

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
