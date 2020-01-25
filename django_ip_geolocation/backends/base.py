"""Base interface for backends."""


class GeolocationBackend(object):
    """Base interface for backends."""

    def __init__(self, ip):
        """Constructor.

        :param ip: Ip address
        :type: str
        """
        self._ip = ip
        self._continent = None
        self._country = None
        self._geo_data = None
        self._raw_data = None

    def geolocate(self):
        """Call geoloaction api. Should be overriden."""
        raise NotImplementedError()

    def _parse(self):
        """Parse raw data and store them in object attributes."""
        raise NotImplementedError()

    def data(self):
        """Return the parsed data.

        :return: Parsed data.
        :rtype: dict
        """
        self._parse()

        return {
            'ip': self._ip,
            'continent': self._continent,
            'county': self._country,
            'geo': self._geo_data,
            'raw_data': self._raw_data
        }
