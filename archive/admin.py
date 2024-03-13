from django.contrib import admin

from .models import (Archive, Interview, Transcript, Person,
                     InterviewInvolvement, Topic, TopicReference)

admin.site.register(Archive)
admin.site.register(Interview)
admin.site.register(Transcript)
admin.site.register(Person)
admin.site.register(Topic)
admin.site.register(InterviewInvolvement)
admin.site.register(TopicReference)
