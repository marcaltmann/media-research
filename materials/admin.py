from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from .models import Transcript


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    search_fields = ["vtt"]
    list_display = ["resource", "language"]
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
