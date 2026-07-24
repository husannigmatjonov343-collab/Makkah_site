from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Favicon so'rovi kelganida 204 (No Content) qaytarish:
    path('favicon.ico', lambda request: HttpResponse(status=204)),
]