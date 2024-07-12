from django.shortcuts import render
from pytube import YouTube
from django.http import FileResponse, HttpResponseBadRequest
import os

def index(request):
    return render(request, 'downloader/index.html')

def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path='videos/')
            file_path = os.path.join('videos', stream.default_filename)
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=stream.default_filename)
        except Exception as e:
            return HttpResponseBadRequest(f"Error: {str(e)}")
    return HttpResponseBadRequest("Invalid request")
