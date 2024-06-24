from django.db import models
from django.utils.translation import gettext_lazy as _

from archive.models import Resource


class Transcript(models.Model):
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        verbose_name=_("resource"),
    )
    json = models.JSONField(
        _("JSON file"),
        default=list,
        help_text=_("Paste the full transcript in JSON format."),
    )
    vtt = models.TextField(
        _("VTT file"),
        default="",
        help_text=_("Paste the full transcript in VTT format."),
    )
    language = models.CharField(_("language"), max_length=5)

    class Meta:
        verbose_name = _("transcript")
        verbose_name_plural = _("transcripts")

    def __str__(self):
        return f"{self.resource} ({self.language})"
