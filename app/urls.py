# ✅ TO'G'RI: app/urls.py
from django.urls import path
from . import views  # Views faylidan funksiyani olasiz

urlpatterns = [
    path('', views.home_page, name='home'), # include EMAS, view funksiyasi bo'lishi kerak!
]