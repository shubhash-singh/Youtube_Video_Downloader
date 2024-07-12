from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VideoForm
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def home(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                yt = YouTube(url)
                streams = yt.streams.filter(progressive=True, file_extension='mp4')
                context = {
                    'form': form,
                    'video': yt,
                    'streams': streams,
                }
                return render(request, 'downloader/home.html', context)
            except VideoUnavailable:
                return HttpResponse("Error: The video is no longer available.", status=410)
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")
    else:
        form = VideoForm()
    return render(request, 'downloader/home.html', {'form': form})

def download(request, stream_id):
    try:
        stream = YouTube(request.GET.get('url')).streams.get_by_itag(stream_id)
        response = HttpResponse(stream.download(), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{stream.default_filename}"'
        return response
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
