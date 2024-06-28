from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Entity, Location, Person


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
    people = Entity.objects.filter(type=Entity.TYPE_PERSON)
    context = {"people": people}
    return render(request, "entities/people/index.html", context)


def person_detail(request, person_id):
    person = get_object_or_404(Entity, pk=person_id)
    context = {"person": person}
    return render(request, "entities/people/detail.html", context)
