import datetime

import factory
from factory.django import DjangoModelFactory

from .models import Resource, Person, Location

class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    date_of_birth = factory.Faker("date_of_birth")


class ResourceFactory(DjangoModelFactory):
    class Meta:
        model = Resource

    title = factory.Faker("name")
    duration = datetime.timedelta(minutes=240)
    pub_date = factory.Faker("date_time",
        tzinfo=datetime.timezone(datetime.timedelta(hours=2), name="CET"))


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.Faker("city")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
