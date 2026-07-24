from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # favicon.png so'rovi kelganda 204 (No Content) qaytaradi va log toza turadi:
]