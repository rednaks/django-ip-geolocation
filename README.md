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

## Settings
You can configure settings for your hook in the `settings.py` as follow:
```python

IP_GEOLOCATION_SETTINGS = {
    'BACKEND': 'django_ip_geolocation.backends.IPGeolocationAPI',
    'BACKEND_API_KEY': '',
    'BACKEND_USERNAME': '',
    'RESPONSE_HEADER': 'X-IP-Geolocation',
    'ENABLE_REQUEST_HOOK': True,
    'ENABLE_RESPONSE_HOOK': True,
}

```

Those are the default settings, that will be overwritten by those set in `settings.py`


| setting                | description                                     | default value (type)                                                  |
|------------------------|-------------------------------------------------|-----------------------------------------------------------------------|
| `BACKEND`              | Backend class used to detect the geolocation    | `django_ip_geolocation.backends.IPGeolocationAPI` (string class path) |
| `BACKEND_API_KEY`      | Api key or token for the backend                | Empty (string)                                                        |
| `BACKEND_USERNAME`     | username for the backend                        | Empty (string)                                                        |
| `RESPONSE_HEADER`      | Custom response header to store the geolocation | `X-IP-Geolocation` (string)                                           |
| `ENABLE_REQUEST_HOOK`  | Enable or disable hook on request               | `True` (bool)                                                         |
| `ENABLE_RESPONSE_HOOK` | Enable or disable hook on request               | `True` (bool)                                                         |

### Available Backends
* `django_ip_geolocation.backends.IPGeolocationAPI` : (Default) Using https://ipgeolocationapi.com/
* `django_ip_geolocation.backends.IPStack` : (Require `BACKEND_API_KEY`) Using https://ipstack.com/documentation


## Implementing your own backend
If you want to add a new backend, you need to inherit from `django_ip_geolocation.backends.base`, then you need to implement `geolocate()` and `_parse()`.
### `geolocate()`
 Makes API calls and stores the API response in `self._raw_data`.

### `_parse()`
Parse raw data stored in `self._raw_data` and assigns values to the class attribute, such as `self._continent`, `self._county`, `self._geo`.

`self._country` is a dict with `code` and `name` keys.

`self._geo` is a dict with `latitude` and `longitude` keys.
