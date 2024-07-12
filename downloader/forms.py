from django import forms

class VideoForm(forms.Form):
    url = forms.URLField(label='YouTube URL', max_length=200)
