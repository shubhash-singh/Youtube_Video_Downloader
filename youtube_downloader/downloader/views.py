# views.py
from django.shortcuts import render
from django.http import FileResponse, HttpResponseBadRequest, HttpResponse
import os
from pytube import YouTube
import youtube_dl
from .forms import DownloadForm
import re

def index(request):
    return render(request, 'downloader/index.html')

def download_video(request):
    form = DownloadForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        if not re.match(regex, video_url):
            return HttpResponse('Enter correct URL.')

        ydl_opts = {}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(video_url, download=False)
            video_audio_streams = []
            for m in meta['formats']:
                file_size = m.get('filesize', 0)
                if file_size is not None:
                    file_size = f'{round(int(file_size) / 1000000, 2)} MB'

                resolution = 'Audio'
                if m.get('height') is not None:
                    resolution = f"{m['height']}x{m['width']}"
                video_audio_streams.append({
                    'resolution': resolution,
                    'extension': m['ext'],
                    'file_size': file_size,
                    'video_url': m['url']
                })
            video_audio_streams = video_audio_streams[::-1]
            context = {
                'form': form,
                'title': meta.get('title', None),
                'streams': video_audio_streams,
                'description': meta.get('description'),
                'likes': f'{int(meta.get("like_count", 0)):,}',
                'dislikes': f'{int(meta.get("dislike_count", 0)):,}',
                'thumb': meta.get('thumbnails')[3]['url'],
                'duration': round(int(meta.get('duration', 1)) / 60, 2),
                'views': f'{int(meta.get("view_count")):,}'
            }
            return render(request, 'home.html', context)
        except Exception as error:
            return HttpResponse(error.args[0])
    return render(request, 'home.html', {'form': form})

# forms.py
from django import forms

class DownloadForm(forms.Form):
    url = forms.URLField(label='Video URL', max_length=200)
