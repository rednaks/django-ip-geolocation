import requests
from .base import GeolocationBackend


class DoAPI(GeolocationBackend):
    def geolocate(self):
        url = 'http://doapi.us/ip/{}/json'.format(self._ip)
        res = requests.get(url)
        if res.ok:
            self._raw_data = res.json()

    def _parse(self):
        _raw_data = self._raw_data or {}
        self._continent = _raw_data.get('continent')
        self._country = {
            'code': _raw_data.get('country_code'),
            'name': _raw_data.get('country'),
        }

