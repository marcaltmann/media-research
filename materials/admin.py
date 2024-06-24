from django.contrib import admin

from .models import Transcript


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    search_fields = ["vtt"]
    list_display = ["resource", "language"]
