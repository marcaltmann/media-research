from django.contrib import admin

from archive.models import (Interview, Collection, Transcript,
                            Person, InterviewInvolvement, Topic,
                            TopicReference, MetadataKey, CharFieldMetadata)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ["title", "media_type", "duration", "public"]
    exclude = ["pub_date"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    fields = ["name", "description", "interviews"]
    list_display = ["name", "interview_count"]
    filter_horizontal = ["interviews"]


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "gender", "date_of_birth"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(InterviewInvolvement)
class InterviewInvolvementAdmin(admin.ModelAdmin):
    pass


@admin.register(TopicReference)
class TopicReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(MetadataKey)
class MetadataKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(CharFieldMetadata)
class CharFieldMetadata(admin.ModelAdmin):
    pass
