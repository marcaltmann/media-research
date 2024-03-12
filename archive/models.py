from datetime import timedelta

from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    gnd_id = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    MALE = "M"
    FEMALE = "F"
    DIVERSE = "D"
    UNSPECIFIED = "N"
    GENDER_CHOICES = {
        MALE: "Male",
        FEMALE: "Female",
        DIVERSE: "Diverse",
        UNSPECIFIED: "Not specified",
    }

    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200)
    gnd_id = models.CharField(max_length=20, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=UNSPECIFIED,
    )
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "people"


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
    media_url = models.URLField(max_length=300, default="")
    poster = models.ImageField(default="", blank=True)
    pub_date = models.DateTimeField("date published")
    duration = models.DurationField(default=timedelta(seconds=0))
    public = models.BooleanField(default=True)
    people = models.ManyToManyField(Person, through="InterviewInvolvement")
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title


class InterviewInvolvement(models.Model):
    INTERVIEWEE = "INT"
    INTERVIEWER = "ITR"
    CAMERA      = "CAM"
    SOUND       = "SND"
    EDITOR      = "EDT"
    OTHER       = "OTH"
    TYPE_CHOICES = {
        INTERVIEWEE: "Interviewee",
        INTERVIEWER: "Interviewer",
        CAMERA:      "Camera",
        SOUND:       "Sound",
        EDITOR:      "Editor",
        OTHER:       "Other",
    }

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES,
                            default=INTERVIEWEE)

    def __str__(self):
        return "{}_{}".format(self.person.__str__(), self.interview.__str__())


class Transcript(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    json = models.JSONField()
    vtt = models.TextField()
    language = models.CharField(max_length=5)
