import requests
from django_ip_geolocation.backends import GeolocationBackend


class IPGeolocationAPI(GeolocationBackend):

    def geolocate(self):
        res = requests.get('https://api.ipgeolocationapi.com/geolocate/{}'.format(self._ip))
        if res.ok:
            self._raw_data = res.json()
            self._parse()

        
    def _parse(self):
        """raw_data example:
        {
            "continent": "Europe",
            "alpha2": "DE",
            "country_code": "49",
            "international_prefix": "00",
            "name": "Germany",
            "languages_spoken": [
                "de"
            ],
            "geo": {
                "latitude": 51.165691,
                "longitude": 10.451526,
            },
            "currency_code": "EUR"
        }
        """
        self._continent = self._raw_data.get('continent')
        self._county = {
            'code': self._raw_data.get('alpha2'),
            'name': self._raw_data.get('name'),
        }

        self._geo_data = self._raw_data.get('geo')

