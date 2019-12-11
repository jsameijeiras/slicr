from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import uuid

def index (request):
    if request.method == 'POST':
        data = request.POST.copy()
        song_file = request.FILES['song']
        fs = FileSystemStorage()
        ext = song_file.name.split('.')[-1]
        song_id = "%s" % uuid.uuid4()
        filename = "%s.%s" % (song_id, ext)
        final_filename = fs.save(filename, song_file)
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        dir_name = "%s" % (song_id)
        outputPath = os.path.join(settings.MEDIA_ROOT, dir_name)
        results = os.system('spleeter separate -i '+filepath+' -p spleeter:4stems -o '+outputPath)
        download_url = fs.url(os.path.join(dir_name, song_id, 'vocals.wav')) # spleeter will generate a dir called as the input filename
        print(download_url)
        return render(request, 'slicr/index.html', {'print_form': False, "download_url": download_url})
    return render(request, 'slicr/index.html', {'print_form': True})
# Create your views here.
