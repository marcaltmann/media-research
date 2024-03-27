from datetime import timedelta
from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    gnd_id = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    geonames_id = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

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
    eastern_name_order = models.BooleanField(default=False)
    gnd_id = models.CharField(max_length=20, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=UNSPECIFIED,
    )
    date_of_birth = models.DateField()

    def fullname(self):
        if self.eastern_name_order:
            return f"{self.last_name} {self.first_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name_plural = "people"


class Interview(models.Model):
    title = models.CharField(max_length=200, default="")
    media_type = models.CharField(max_length=100, default="video/mp4")
    media_url = models.URLField(max_length=300, default="")
    poster = models.ImageField(default="", blank=True)
    pub_date = models.DateTimeField("date published")
    duration = models.DurationField(default=timedelta(seconds=0))
    public = models.BooleanField(default=True)
    people = models.ManyToManyField(Person, through="InterviewInvolvement")
    topics = models.ManyToManyField(Topic, through="TopicReference")
    locations = models.ManyToManyField(Location, through="LocationReference")

    def media_type_first_part(self) -> str:
        return self.media_type.split("/")[0]

    def is_video(self) -> bool:
        return self.media_type_first_part() == "video"

    def is_audio(self) -> bool:
        return self.media_type_first_part() == "audio"

    def char_field_metadata(self):
        return self.charfieldmetadata_set.all()

    def __str__(self):
        return self.title


class Collection(models.Model):
    interviews = models.ManyToManyField(Interview)
    name = models.CharField(max_length=200)
    description = models.TextField(default="")

    def interview_count(self):
        return self.interviews.count()

    def __str__(self):
        return self.name


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


class TopicReference(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    timecode = models.DecimalField(max_digits=10, decimal_places=3, null=True,
                                   blank=True)

    def __str__(self):
        return f"{self.topic}_{self.interview} ({self.timecode})"


class LocationReference(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    timecode = models.DecimalField(max_digits=10, decimal_places=3,
                                   null=True, blank=True)

    def __str__(self):
        return f"{self.location}_{self.interview} ({self.timecode})"


class Transcript(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    json = models.JSONField()
    vtt = models.TextField()
    language = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.interview} ({self.language})"


class MetadataKey(models.Model):
    label = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def char_fields_for_interview(self, interview_id):
        return self.charfieldmetadata_set.all().filter(interview_id=interview_id)

    def __str__(self):
        return self.label


class CharFieldMetadata(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = "char field metadata"
