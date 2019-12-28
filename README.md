# Django Ip Geolocation:
Django request/response hooks to geolocate visitors by their ip address

# Usage:
## Decorator:
Use decorators to decorate views :
```python
from django_ip_geolocation.decorators import with_ip_geolocation

@with_ip_geolocation
def api_view(request):
   location = request.location
   ...
```

## Middleware:

First you need to add the middleware into your `settings.py`
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
   location = request.location
   ...
   
def other_view(request):
  location = request.location
  ...
```

## Settings
You can configure backend for your hook in the `settings.py` as follow:
```python

GEOLOCATION_BACKEND = 'django_ip_geolocation.backends.IPGeolocationAPI'
```

### Available Backends:
* `django_ip_geolocation.backends.IPGeolocationAPI` : (Default) Using https://ipgeolocationapi.com/
