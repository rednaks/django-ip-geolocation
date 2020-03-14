import unittest

from django.http import HttpResponse

from django.test import TestCase
import logging
from django_ip_geolocation.settings import IP_GEOLOCATION_SETTINGS
from tests.utils import change_settings


class GeolocationTests(TestCase):

    def setUp(self):
        self._default_settings = IP_GEOLOCATION_SETTINGS.copy()


    def test_geolocation_in_response(self):
        response = self.client.get('/test_geolocation/')
        self.assertTrue(response.has_header('X-IP-Geolocation'))
        if response.has_header('X-IP-Geolocation'):
            print(response['X-IP-Geolocation'])

    @change_settings(settings={'ENABLE_REQUEST_HOOK': False})
    def test_geolocation_in_response_when_request_disabled(self):
        response = self.client.get('/test_geolocation/')
        self.assertTrue(response.has_header('X-IP-Geolocation'))
        if response.has_header('X-IP-Geolocation'):
            print(response['X-IP-Geolocation'])

    @change_settings(settings={'ENABLE_RESPONSE_HOOK': False})
    def test_geolocation_not_in_response_when_response_disabled(self):
        response = self.client.get('/test_geolocation/')
        self.assertFalse(response.has_header('X-IP-Geolocation'))

    def test_cookie_not_in_response(self):
        response = self.client.get('/test_geolocation/')
        self.assertIsNone(response.cookies.get('geolocation'))

    @change_settings(settings={'ENABLE_COOKIE': True})
    def test_cookie_in_response(self):
        response = self.client.get('/test_geolocation/')
        self.assertIsNotNone(response.cookies.get('geolocation'))
