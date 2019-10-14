from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title' : 'Wakes Home'
    }
    return render(request, 'feed/base.html', context)

# Create your views here.
