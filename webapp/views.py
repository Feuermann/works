from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/basic.html', {'kek':['if you wanna do something.','JUST DO IT!!!!']})