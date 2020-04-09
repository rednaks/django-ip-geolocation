[![PyPI version](https://badge.fury.io/py/django-ip-geolocation.svg)](https://badge.fury.io/py/django-ip-geolocation) [![Downloads](https://pepy.tech/badge/django-ip-geolocation)](https://pepy.tech/project/django-ip-geolocation) [![Build Status](https://travis-ci.org/rednaks/django-ip-geolocation.svg?branch=release)](https://travis-ci.org/rednaks/django-ip-geolocation)

# Django Ip Geolocation
Django request/response hooks to geolocate visitors by their ip address.

# Installing
```
python -m pip install django-ip-geolocation
``` 

# Usage
## Decorator
Use decorators to decorate views:
```python
from django_ip_geolocation.decorators import with_ip_geolocation

@with_ip_geolocation
def api_view(request):
   location = request.geolocation
   ...
```

## Middleware

First you need to add the middleware into your `settings.py`.
```python
MIDDLEWARE = [
    ...
    'django_ip_geolocation.middleware.IpGeolocationMiddleware',
    ...
]
```

Then the location is available to all views in request and response:
```python
def api_view(request):
   location = request.geolocation
   ...
   
def other_view(request):
  location = request.geolocation
  ...
```

## Cookie
Geolocation data stored in the Response cookie lacks the `raw_data` and is base64 encoded.


## User consent
Developers must implement a helper function to check if the user consented or not and configure it in the `settings.py`. 

By default if the developer didn't provide a validation function, we consider it as implicit consent.

Here is an example of the helper function:

```python

def check_user_consent(request):
  if request.user.is_consented: # this is only an example.
    return True
  return False

```



## Settings
You can configure settings for your hook in the `settings.py` as follow:
```python

IP_GEOLOCATION_SETTINGS = {
    'BACKEND': 'django_ip_geolocation.backends.IPGeolocationAPI',
    'BACKEND_API_KEY': '',
    'BACKEND_EXTRA_PARAMS': {},
    'BACKEND_USERNAME': '',
    'RESPONSE_HEADER': 'X-IP-Geolocation',
    'ENABLE_REQUEST_HOOK': True,
    'ENABLE_RESPONSE_HOOK': True,
    'ENABLE_COOKIE': False,
    'FORCE_IP_ADDR': None,
    'USER_CONSENT_VALIDATOR': None
}

```

Those are the default settings, that will be overwritten by those set in `settings.py`


| setting                | description                                     | default value (type)                                                  |
|------------------------|-------------------------------------------------|-----------------------------------------------------------------------|
| `BACKEND`              | Backend class used to detect the geolocation    | `django_ip_geolocation.backends.IPGeolocationAPI` (string class path) |
| `BACKEND_API_KEY`      | Api key or token for the backend                | Empty (string)                                                        |
| `BACKEND_EXTRA_PARAMS` | Extra parameters specific to the backend        | `{}` (dict)                                                           |
| `BACKEND_USERNAME`     | username for the backend                        | Empty (string)                                                        |
| `RESPONSE_HEADER`      | Custom response header to store the geolocation | `X-IP-Geolocation` (string)                                           |
| `ENABLE_REQUEST_HOOK`  | Enable or disable hook on request               | `True` (bool)                                                         |
| `ENABLE_RESPONSE_HOOK` | Enable or disable hook on request               | `True` (bool)                                                         |
| `ENABLE_COOKIE`        | Enable or disable geolocation data in cookie    | `False` (bool)                                                        |
| `FORCE_IP_ADDR`        | Force ip address, rather than using visitor ip  | `None` (string)                                                       |
| `USER_CONSENT_VALIDATOR`| A function path to check if the current user gave his consent  | `None` (string, function path)                        |

### Available Backends
* `django_ip_geolocation.backends.IPGeolocationAPI` : (Default) Using https://ipgeolocationapi.com/
* `django_ip_geolocation.backends.IPStack` : (Require `BACKEND_API_KEY`) Using https://ipstack.com/documentation
* `django_ip_geolocation.backends.IP2LocationCom` : (Require `BACKEND_API_KEY`, Accepts `BACKEND_EXTRA_PARAMS`) Using https://www.ip2location.com/web-service/ip2location
* `django_ip_geolocation.backends.IPDataCo` : (Require `BACKEND_API_KEY`) Using https://docs.ipdata.co/


## Implementing your own backend
If you want to add a new backend, you need to inherit from `django_ip_geolocation.backends.base`, then you need to implement `geolocate()` and `_parse()`.
### `geolocate()`
 Makes API calls and stores the API response in `self._raw_data`.

### `_parse()`
Parse raw data stored in `self._raw_data` and assigns values to the class attribute, such as `self._continent`, `self._county`, `self._geo`.

`self._country` is a dict with `code` and `name` keys.

`self._geo` is a dict with `latitude` and `longitude` keys.
