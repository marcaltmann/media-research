from datetime import timedelta
from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from entities.models import Location, Person


class Resource(models.Model):
    title = models.CharField(max_length=200, default="")
    anon_title = models.CharField(max_length=200, default="")
    media_type = models.CharField(
        max_length=100,
        default="video/mp4",
        help_text="Enter MIME type e.g. 'video/mp4'.",
    )
    media_url = models.URLField(max_length=300, default="")
    poster = models.ImageField(default="", blank=True)
    pub_date = models.DateTimeField("date published", null=True)
    duration = models.DurationField(default=timedelta(seconds=0))
    public = models.BooleanField(default=True)
    people = models.ManyToManyField(Person, through="ResourceInvolvement")
    locations = models.ManyToManyField(Location, through="LocationReference")

    class Meta:
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"]),
        ]
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")

    def media_type_first_part(self) -> str:
        return self.media_type.split("/")[0]

    @admin.display(
        boolean=True,
        ordering="media_type",
        description="is video?",
    )
    def is_video(self) -> bool:
        return self.media_type_first_part() == "video"

    def is_audio(self) -> bool:
        return self.media_type_first_part() == "audio"

    def char_field_metadata(self):
        return self.charfieldmetadata_set.all()

    def get_absolute_url(self):
        return reverse("archive:resource_detail", args=[self.id])

    def __str__(self):
        return self.title


class Collection(models.Model):
    resources = models.ManyToManyField(Resource)
    name = models.CharField(max_length=200)
    description = models.TextField(default="")

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def resource_count(self):
        return self.resources.count()

    def get_absolute_url(self):
        return reverse("archive:collection_detail", args=[self.id])

    def __str__(self):
        return self.name


class ResourceInvolvement(models.Model):
    INTERVIEWEE = "INT"
    INTERVIEWER = "ITR"
    CAMERA = "CAM"
    SOUND = "SND"
    EDITOR = "EDT"
    OTHER = "OTH"
    TYPE_CHOICES = {
        INTERVIEWEE: "Interviewee",
        INTERVIEWER: "Interviewer",
        CAMERA: "Camera",
        SOUND: "Sound",
        EDITOR: "Editor",
        OTHER: "Other",
    }

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=INTERVIEWEE)

    def __str__(self):
        return "{}_{}".format(self.person.__str__(), self.resource.__str__())


class LocationReference(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    timecode = models.DecimalField(
        max_digits=10, decimal_places=3, null=True, blank=True
    )

    def __str__(self):
        return f"{self.location}_{self.resource} ({self.timecode})"


class Transcript(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    json = models.JSONField()
    vtt = models.TextField()
    language = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.resource} ({self.language})"


class MetadataKey(models.Model):
    label = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def char_fields_for_resource(self, resource_id):
        return self.charfieldmetadata_set.all().filter(resource_id=resource_id)

    def __str__(self):
        return self.label


class CharFieldMetadata(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = "char field metadata"
