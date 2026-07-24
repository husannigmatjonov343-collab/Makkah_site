# ✅ TO'G'RI: Makkah_site/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Bu yerda ILOVA (APP) nomi bo'lishi kerak!
    path('', include('sayt_ilovasi.urls')), 
]