import requests
from base import GeolocationBackend


class IPGeolocationAPI(GeolocationBackend):
    def __init__(self, ip):
        self._ip = ip

    def geolocate(self):
        res = requests.get('https://api.ipgeolocationapi.com/geolocate/{}'.format(self._ip))
        if res.ok:
            return res.json()

