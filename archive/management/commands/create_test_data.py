import datetime
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from faker import Faker

from archive.models import (
    Person, Resource, Topic, Location, Collection, MetadataKey,
    ResourceInvolvement,
)

NUM_PEOPLE = 1000
NUM_LOCATIONS = 1000
NUM_COLLECTIONS = 20


def create_people():
    """Creates fake person records."""
    fake = Faker()
    people = []
    for _ in range(NUM_PEOPLE):
        person = Person.objects.create(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            date_of_birth = fake.date_of_birth(minimum_age=20),
        )
        people.append(person)
    return people


def create_resources(people):
    """Creates fake resource records."""
    fake = Faker()
    resources = []
    for person in people:
        first_name = person.first_name
        last_name = person.last_name
        resource = Resource.objects.create(
            title=f"{first_name} {last_name}",
            anon_title=f"{first_name} {last_name[0]}.",
            duration=datetime.timedelta(minutes=random.randint(10, 360)),
            pub_date=fake.date_time(tzinfo=datetime.timezone(
                datetime.timedelta(hours=2), name="CET"))
        )
        role = ResourceInvolvement.objects.create(
            person=person,
            resource=resource,
            type=ResourceInvolvement.INTERVIEWEE,
        )
        resources.append(resource)
    return resources


def create_locations():
    """Creates fake location records."""
    fake = Faker()
    locations = []
    for _ in range(NUM_PEOPLE):
        latitude, longitude, name, _, _ = fake.location_on_land()
        location = Location.objects.create(
            name=name,
            latitude=latitude,
            longitude=longitude,
        )
        locations.append(location)
    return locations


def create_collections():
    """Creates fake collection records."""
    fake = Faker()
    collections = []
    for _ in range(NUM_COLLECTIONS):
        collection = Collection.objects.create(
            name=fake.catch_phrase(),
            description=fake.paragraph(nb_sentences=5,
                                       variable_nb_sentences=True),
        )
        collections.append(collection)
    return collections


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Person, Resource, Topic, Location, Collection, MetadataKey]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        people = create_people()
        resources = create_resources(people)
        locations = create_locations()
        collections = create_collections()
