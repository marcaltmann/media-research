import datetime
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from faker import Faker

from archive.models import (
    Person,
    Resource,
    Location,
    Collection,
    MetadataKey,
    ResourceInvolvement,
)

NUM_PEOPLE = 500_000
NUM_LOCATIONS = 50
NUM_COLLECTIONS = 20


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Person, Resource, Location, Collection, MetadataKey]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        people = create_people()
        locations = create_locations()
        resources = create_resources(people, locations)
        collections = create_collections(resources)


def create_people():
    """Creates fake person records."""
    fake = Faker()
    people = []
    for _ in range(NUM_PEOPLE):
        person = Person.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(minimum_age=20),
        )
        people.append(person)
    return people


def create_resources(people, locations):
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
            media_type=fake.mime_type(
                category=random.choice(("video", "audio")),
            ),
            pub_date=fake.date_time(
                tzinfo=datetime.timezone(datetime.timedelta(hours=2), name="CET")
            ),
        )
        resources.append(resource)

        role = ResourceInvolvement.objects.create(
            person=person,
            resource=resource,
            type=ResourceInvolvement.INTERVIEWEE,
        )
        # locationRef = LocationReference.objects.create(
        #     location=random.choice(locations),
        #     resource=resource,
        # )
    return resources


def create_locations():
    """Creates fake location records."""
    fake = Faker()
    locations = []
    for _ in range(NUM_LOCATIONS):
        latitude, longitude, name, _, _ = fake.location_on_land()
        location = Location.objects.create(
            name=name,
            latitude=latitude,
            longitude=longitude,
        )
        locations.append(location)
    return locations


def create_collections(resources):
    """Creates fake collection records."""
    fake = Faker()
    collections = []
    for _ in range(NUM_COLLECTIONS):
        collection = Collection.objects.create(
            name=fake.catch_phrase(),
            description=fake.paragraph(nb_sentences=5, variable_nb_sentences=True),
        )
        collections.append(collection)
        resources_pick = random.choices(resources, k=random.randint(2, 60))
        collection.resources.add(*resources_pick)
    return collections
