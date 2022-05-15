from django.db import models

# Model for Blog component
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

# Model for uploading videos component
class Video(models.Model):
    video_name = models.CharField(max_length=250) # limit video name to 250 chars
    video_file = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.video_file)