from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )