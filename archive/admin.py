from django.contrib import admin

from archive.models import (Archive, Interview, Transcript, Person,
                     InterviewInvolvement, Topic, TopicReference,
                     MetadataKey, CharFieldMetadata)


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    exclude = ["pub_date"]


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


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
