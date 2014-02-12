# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'msg': "No query yet."})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        message = 'You search for: %r' % request.GET['q']
        print("AEAEAE")
        return render(request, 'search.html', {'msg':message})
    else:
        message = 'You submited an empty form'
        print("AAAAAAH")
        return render(request, 'home.html', {'msg':message})


