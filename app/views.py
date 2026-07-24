# app/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Makkah site muvaffaqiyatli ishga tushdi!")