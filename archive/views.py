from django.shortcuts import get_object_or_404, get_list_or_404, render

from archive.models import Interview, Collection, Person, Topic

def welcome(request):
    return render(request, "archive/welcome.html")

def collection_index(request):
    collections = get_list_or_404(Collection)
    return render(request, "archive/collection_index.html",
                  {"collections": collections})

def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    context = {
        "collection": collection,
        "interviews": collection.interviews.all(),
    }
    return render(request, "archive/collection_detail.html", context)

def interview_index(request):
    interviews = get_list_or_404(Interview)
    return render(request, "archive/interview_index.html",
                  {"interviews": interviews})

def interview_detail(request, interview_id):
    interview = get_object_or_404(Interview, pk=interview_id)
    context = {
        "interview": interview,
        "collections": interview.collection_set.all(),
    }
    return render(request, "archive/interview_detail.html", context)

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
