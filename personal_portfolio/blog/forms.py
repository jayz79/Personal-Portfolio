# ModelForm file, used for the video database
from django import forms
from .models import Video
class VideoForm(forms.ModelForm):

    class MetaData:
        model = Video.objects
        fields = ["name", "videofile"]