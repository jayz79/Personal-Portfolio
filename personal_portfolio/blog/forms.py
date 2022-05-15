# ModelForm file, used for the video database

class VideoForm(forms.ModelForm):

    class MetaData:
        model = Video
        fields = ["name", "videofile"]