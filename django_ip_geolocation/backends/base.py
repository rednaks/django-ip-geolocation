class NotImplementedException(Exception):
    pass


class GeolocationBackend(object):
    def __init__(self, ip):
        self._ip = ip
        self._continent = None
        self._country = None
        self._geo_data = None
        self._raw_data = None

    def geolocate(self):
        raise NotImplementedException()

    def _parse(self):
        raise NotImplementedException()

    def data(self):
        self._parse()

        return {
            'ip': self._ip,
            'continent': self._continent,
            'county': self._country,
            'geo': self._geo_data,
            'raw_data': self._raw_data
        }
