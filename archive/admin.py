from django.contrib import admin

from archive.models import (Interview, Collection, Transcript,
                            Person, InterviewInvolvement, Topic,
                            TopicReference, MetadataKey, CharFieldMetadata)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "media_type", "duration", "public"]
    exclude = ["pub_date"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]
    fields = ["name", "description", "interviews"]
    list_display = ["name", "interview_count"]
    filter_horizontal = ["interviews"]


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    search_fields = ["vtt"]
    list_display = ["interview", "language"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "first_name"]
    list_display = ["last_name", "first_name", "gender", "date_of_birth"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["name", "gnd_id"]
    list_display = ["name", "gnd_id"]


@admin.register(InterviewInvolvement)
class InterviewInvolvementAdmin(admin.ModelAdmin):
    autocomplete_fields = ["person", "interview"]
    list_display = ["person", "interview", "type"]


@admin.register(TopicReference)
class TopicReferenceAdmin(admin.ModelAdmin):
    autocomplete_fields = ["topic"]
    list_display = ["topic", "interview", "timecode"]


@admin.register(MetadataKey)
class MetadataKeyAdmin(admin.ModelAdmin):
    search_fields = ["label"]
    list_display = ["label"]


@admin.register(CharFieldMetadata)
class CharFieldMetadata(admin.ModelAdmin):
    list_display = ["interview", "key", "value"]
