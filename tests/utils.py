from django_ip_geolocation.settings import IP_GEOLOCATION_SETTINGS


def change_settings(settings):
    def decorator(func):
        def wrapper(*args, **kwargs):
            default_settings = args[0]._default_settings
            IP_GEOLOCATION_SETTINGS.update(settings)
            func(*args, **kwargs)
            IP_GEOLOCATION_SETTINGS.update(default_settings)
        return wrapper
    return decorator