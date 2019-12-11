from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    hello = "Hello, world esto es un cambio"
    return render(request, 'slicr/index.html', {'hello':hello})
# Create your views here.
