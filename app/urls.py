from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views  # agar views shu papkada bo'lsa

urlpatterns = [
    # 1. Asosiy Bosh sahifa (Shu yetishmayotgan edi!):
    path('', views.home, name='home'),

    # 2. Favicon xatolarini yutib yuboradigan yo'llar:
    path('favicon.ico', lambda r: HttpResponse(status=204)),
    path('favicon.png', lambda r: HttpResponse(status=204)),
]