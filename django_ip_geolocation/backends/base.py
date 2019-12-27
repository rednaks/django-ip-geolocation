
class NotImplementedException(Exception):
    pass

class GeolocationBackend(object):
    def __init__(self, ip):
        self._ip = ip

    def geolocate(self):
        raise NotImplementedException

