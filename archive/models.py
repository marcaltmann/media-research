from datetime import timedelta

from django.db import models

class Archive(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    public = models.BooleanField()

    def __str__(self):
        return self.name


class Interview(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="")
    media_type = models.CharField(max_length=100, default="video/mp4")
    media_url = models.URLField(default="")
    poster = models.ImageField(default="", blank=True)
    pub_date = models.DateTimeField("date published")
    duration = models.DurationField(default=timedelta(seconds=0))
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
