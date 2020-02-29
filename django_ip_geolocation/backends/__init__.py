"""All backends modules."""
from django_ip_geolocation.backends.base import GeolocationBackend
from django_ip_geolocation.backends.ipgeolocationapi import IPGeolocationAPI
from django_ip_geolocation.backends.ipstack import IPStack
from django_ip_geolocation.backends.ip2locationcom import IP2LocationCom
from django_ip_geolocation.backends.ipdataco import IPDataCo


__all__ = ['GeolocationBackend', 'IPGeolocationAPI',
           'IPStack', 'IP2LocationCom', 'IPDataCo']
