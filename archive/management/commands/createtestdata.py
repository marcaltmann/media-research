import datetime
import random

from django.db import transaction
from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone

from archive.models import (
    Person,
    Resource,
    Topic,
    Location,
    Collection,
    MetadataKey,
    ResourceInvolvement,
    LocationReference,
)


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Person, Resource, Topic, Location, Collection, MetadataKey]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        create_people()
        create_resources()


def create_people():
    """Creates person records."""
    Person.objects.bulk_create([
        Person(
            first_name="Winston",
            last_name="Churchill",
            date_of_birth=datetime.date(1874, 11, 13),
            gender="M",
            gnd_id="118520776",
        ),
        Person(
            first_name="Michael",
            last_name="Kende",
            date_of_birth=datetime.date(1974, 3, 13),
            gender="M",
            gnd_id="171121503",
        ),
        Person(
            first_name="John",
            last_name="Malkovich",
            date_of_birth=datetime.date(1953, 12, 9),
            gender="M",
            gnd_id="128617381",
        ),
        Person(
            first_name="Minoru",
            last_name="Arakawa",
            date_of_birth=datetime.date(1946, 9, 3),
            gender="M",
            gnd_id="",
        ),
        Person(
            first_name="Maximilian",
            last_name="Schönherr",
            date_of_birth=datetime.date(1954, 12, 27),
            gender="M",
            gnd_id="130608939",
        ),
        Person(
            first_name="貝兒",
            last_name="陳",
            date_of_birth=datetime.date(1990, 3, 14),
            gender="F",
            gnd_id="",
            eastern_name_order=True,
        ),
    ])


def create_resources():
    """Creates resource records."""
    churchill = Person.objects.get(last_name="Churchill")
    kende = Person.objects.get(last_name="Kende")
    malkovich = Person.objects.get(last_name="Malkovich")
    arakawa = Person.objects.get(last_name="Arakawa")
    schoenherr = Person.objects.get(last_name="Schönherr")
    fang = Person.objects.get(last_name="陳")

    Resource.objects.bulk_create([
        Resource(
            title="Michael Kende (Internet Society)",
            media_type="video/webm",
            media_url="https://upload.wikimedia.org/wikipedia/commons/transcoded/6/6d/Internet_Hall_of_Fame_2014_Michael_Kende_interview.webm/Internet_Hall_of_Fame_2014_Michael_Kende_interview.webm.720p.vp9.webm",
            poster="doggy.jpg",
            pub_date=datetime.datetime(2024, 3, 8, 12, 6, 35, tzinfo=get_current_timezone()),
            duration=datetime.timedelta(minutes=3, seconds=55),
            public=True,
        ),
        Resource(
            title="John Malkovich",
            media_type="video/webm",
            media_url="https://upload.wikimedia.org/wikipedia/commons/7/74/John_Malkovich_-_Les_Liaisons_dangereuses.webm",
            poster="doggy.jpg",
            pub_date=datetime.datetime(2024, 3, 9, 7, 42, 22, tzinfo=get_current_timezone()),
            duration=datetime.timedelta(minutes=7, seconds=11),
            public=True,
        ),
        Resource(
            title="Minoru Arakawa (Nintendo)",
            media_type="audio/mp3",
            media_url="https://upload.wikimedia.org/wikipedia/commons/5/5c/Minoru_Arakawa_%E2%80%93_Nintendo_%E2%80%93_Gameboy%2C_interviewed_by_Maximilian_Sch%C3%B6nherr_1990.mp3",
            poster="",
            pub_date=datetime.datetime(2024, 3, 14, 17, 38, 53, tzinfo=get_current_timezone()),
            duration=datetime.timedelta(minutes=3, seconds=46),
            public=True,
        ),
        Resource(
            title="灣區青年說 · 對話香港 TVB 主持人陳貝兒",
            media_type="audio/ogg",
            media_url="https://upload.wikimedia.org/wikipedia/commons/2/2a/%E7%81%A3%E5%8D%80%E9%9D%92%E5%B9%B4%E8%AA%AA_%C2%B7_%E5%B0%8D%E8%A9%B1%E9%A6%99%E6%B8%AF_TVB_%E4%B8%BB%E6%8C%81%E4%BA%BA%E9%99%B3%E8%B2%9D%E5%85%92.ogg",
            poster="",
            pub_date=datetime.datetime(2024, 3, 14, 19, 27, 51, tzinfo=get_current_timezone()),
            duration=datetime.timedelta(minutes=42, seconds=4),
            public=True,
        ),
    ])


def create_locations():
    """Creates location records."""
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
    """Creates collection records."""
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
