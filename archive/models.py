from django.db import models

class Archive(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    public = models.BooleanField()

    def __str__(self):
        return self.name


class Interview(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    public = models.BooleanField()

    def __str__(self):
        return self.title
