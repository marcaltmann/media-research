from datetime import timedelta
from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from entities.models import Entity, Location, Person


class Resource(models.Model):
    title = models.CharField(_("title"), max_length=200, default="")
    anon_title = models.CharField(_("anonymized title"), max_length=200, default="")
    media_type = models.CharField(
        _("media type"),
        max_length=100,
        default="video/mp4",
        help_text="Enter MIME type e.g. 'video/mp4'.",
    )
    media_url = models.URLField(_("media url"), max_length=300, default="")
    poster = models.ImageField(_("poster image"), default="", blank=True)
    pub_date = models.DateTimeField(_("date published"), null=True)
    duration = models.DurationField(_("duration"), default=timedelta(seconds=0))
    public = models.BooleanField(_("public"), default=True)
    people = models.ManyToManyField(
        Person, through="ResourceInvolvement", verbose_name=_("people")
    )

    class Meta:
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"]),
        ]
        verbose_name = _("resource")
        verbose_name_plural = _("resources")

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
    resources = models.ManyToManyField(Resource, verbose_name=_("resources"))
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"), default="")

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = _("collection")
        verbose_name_plural = _("collections")

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


class EntityReference(models.Model):
    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, verbose_name=_("entity")
    )
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, verbose_name=_("resource")
    )
    timecodes = models.JSONField(
        _("timecodes"),
        default=list,
        help_text=_(
            "Enter timecodes in seconds as a comma separated list, e.g.: [124.3, 210.5]"
        ),
    )

    class Meta:
        verbose_name = _("entity reference")
        verbose_name_plural = _("entity references")

    def __str__(self):
        return f"{self.entity}_{self.resource}"


class Transcript(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, verbose_name=_("resource")
    )
    json = models.JSONField(
        _("json file"),
        default=list,
        help_text=_("Paste the full transcript in JSON format."),
    )
    vtt = models.TextField(
        _("vtt file"),
        default="",
        help_text=_("Paste the full transcript in VTT format."),
    )
    language = models.CharField(_("language"), max_length=5)

    class Meta:
        verbose_name = _("transcript")
        verbose_name_plural = _("transcripts")

    def __str__(self):
        return f"{self.resource} ({self.language})"


class MetadataKey(models.Model):
    label = models.CharField(_("label"), max_length=20)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        verbose_name = _("metadata key")
        verbose_name_plural = _("metadata keys")

    def char_fields_for_resource(self, resource_id):
        return self.charfieldmetadata_set.all().filter(resource_id=resource_id)

    def __str__(self):
        return self.label


class CharFieldMetadata(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, verbose_name=_("resource")
    )
    key = models.ForeignKey(
        MetadataKey, on_delete=models.CASCADE, verbose_name=_("key")
    )
    value = models.CharField(_("value"), max_length=200)

    class Meta:
        verbose_name = _("char field metadata")
        verbose_name_plural = _("char field metadata")

    def __str__(self):
        return self.value
