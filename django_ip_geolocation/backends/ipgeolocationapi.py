import requests
from django_ip_geolocation.backends import GeolocationBackend


class IPGeolocationAPI(GeolocationBackend):

    def geolocate(self):
        res = requests.get('https://api.ipgeolocationapi.com/geolocate/{}'.format(self._ip))
        if res.ok:
            return res.json()

