from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def geolocation_test(request):
    """
    Initialize request.
    """
    response = HttpResponse("hello skander")
    return response
