from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import uuid

def get_song_id():
    song_id = "%s" % uuid.uuid4()
    return song_id

def get_output_dir_base_path(song_id):
    return os.path.join(settings.MEDIA_ROOT, song_id)

def get_output_dir_path(song_id):
    return os.path.join(get_output_dir_base_path(song_id), song_id)

def get_output_relative_file_paths(song_id):
    output_path = get_output_dir_path(song_id)
    files = os.listdir(output_path)
    relative_file_paths = [os.path.join(song_id, song_id, file) for file in files if file.endswith('.wav')]
    return relative_file_paths

def index_view(request):
    return render(request, 'slicr/form.html')


def download_view(request):
    if request.method != 'POST':
        return HttpResponse('Invalid page')
    # POST request
    data = request.POST.copy()
    song_file = request.FILES['song']
    fs = FileSystemStorage()
    ext = song_file.name.split('.')[-1]
    song_id = get_song_id()
    print('Processing song id '+song_id)
    filename = "%s.%s" % (song_id, ext)
    fs.save(filename, song_file)
    input_file_path = os.path.join(settings.MEDIA_ROOT, filename)
    print('Input file path: '+input_file_path)
    dir_name = "%s" % (song_id)
    output_dir_base_path = get_output_dir_base_path(song_id)
    cmd = 'spleeter separate -i '+input_file_path+' -p spleeter:4stems -o '+output_dir_base_path
    print('Running command: '+cmd)
    os.system(cmd)
    download_links = [{
        'url': fs.url(output_relative_file_path),
        'name': output_relative_file_path.split('/')[-1]
        } for output_relative_file_path in get_output_relative_file_paths(song_id)]
    return render(
        request,
        'slicr/download.html',
        { 'download_links': download_links }
    )

def about_view(request):
    return render(request, 'slicr/about.html')
