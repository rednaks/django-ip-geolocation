import requests
from base import GeolocationBackend


class IPGeolocationAPI(GeolocationBackend):
    def __init__(self, ip):
        self._ip = ip

    def geolocate(self):
        logging.error("geolocating ip: %s", self._ip)
        res = requests.get('https://api.ipgeolocationapi.com/geolocate/{}'.format(self._ip))
        if res.ok:
            logging.error(res.json())
            return res.json()

