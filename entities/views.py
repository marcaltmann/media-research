from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Person, Topic, Location


def index(request):
    return render(request, "entities/index.html")


class LocationIndexView(generic.ListView):
    template_name = "entities/location_index.html"
    context_object_name = "location_list"
    paginate_by = 25

    def get_queryset(self) -> QuerySet[Location]:
        """Return all locations."""
        return Location.objects.order_by("name")


class LocationDetailView(generic.DetailView):
    model = Location


def person_index(request):
    people = Person.objects.all
    context = {"people": people}
    return render(request, "entities/people/index.html", context)


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    context = {"person": person}
    return render(request, "entities/people/detail.html", context)


def topic_index(request):
    topics = Topic.objects.all
    context = {"topics": topics}
    return render(request, "entities/topics/index.html", context)


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {"topic": topic}
    return render(request, "entities/topics/detail.html", context)
