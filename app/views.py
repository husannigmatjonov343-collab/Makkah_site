from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # index.html o'rniga o'zingizning HTML faylingiz nomini yozing