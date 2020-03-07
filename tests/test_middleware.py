import unittest

from django.http import HttpResponse

from django.test import TestCase, override_settings
import logging


class GeolocationTests(TestCase):

    def test_response(self):
        response = self.client.get('/test_geolocation/')
        self.assertTrue(response.has_header('X-IP-Geolocation'))
        if response.has_header('X-IP-Geolocation'):
            print(response['X-IP-Geolocation'])

    def test_cookie_not_in_response(self):
        response = self.client.get('/test_geolocation/')
        self.assertIsNone(response.cookies.get('geolocation'))
            

