from django.shortcuts import get_object_or_404, render

from .models import Archive, Interview, Person, Topic

def welcome(request):
    return render(request, "archive/welcome.html")

def index(request):
    all_archives = Archive.objects.all
    context = {
        "archives": all_archives
    }
    return render(request, "archive/index.html", context)

def detail(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, "archive/detail.html", {"archive": archive})

def interview_index(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, "archive/interview_index.html",
                  {"archive": archive})

def interview_detail(request, archive_id, interview_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    interview = get_object_or_404(Interview, pk=interview_id)
    return render(request, "archive/interview_detail.html",
                  {"archive": archive, "interview": interview})

def person_index(request):
    people = Person.objects.all
    context = {"people": people}
    return render(request, "archive/people/index.html", context)

def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    context = {"person": person}
    return render(request, "archive/people/detail.html", context)

def topic_index(request):
    topics = Topic.objects.all
    context = {"topics": topics}
    return render(request, "archive/topics/index.html", context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {"topic": topic}
    return render(request, "archive/topics/detail.html", context)
