from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome home!")
    # Or if you're using a template:
    # return render(request, 'home.html')