from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    # ... sizning boshqa url'laringiz ...

    # Favicon so'rovlarini e'tiborsiz qoldirish (Bo'sh 204 javob qaytaradi):
    path('favicon.ico', lambda r: HttpResponse(status=204)),
    path('favicon.png', lambda r: HttpResponse(status=204)),
]