from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def index (request):
    if request.method == 'POST':

        data = request.POST.copy()
        firstname = data.get("firstname")
        hello = "POST request"
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        return render(request, 'slicr/index.html', {'hello':hello, 'filepath': filepath, 'print_form': False})
    hello = "GET request"
    return render(request, 'slicr/index.html', {'hello':hello, 'print_form': True})
# Create your views here.
