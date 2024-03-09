from django.contrib import admin

from .models import (Archive, Interview, Person, InterviewInvolvement,
                     Topic)

admin.site.register(Archive)
admin.site.register(Interview)
admin.site.register(Person)
admin.site.register(Topic)
admin.site.register(InterviewInvolvement)
