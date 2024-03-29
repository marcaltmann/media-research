import datetime
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from archive.models import (
    Person, Interview, Topic, Location, Collection, MetadataKey
)
from archive.factories import PersonFactory, LocationFactory, InterviewFactory

NUM_PEOPLE = 1000
NUM_LOCATIONS = 1000

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Person, Interview, Topic, Location, Collection, MetadataKey]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        # Create people
        people = []
        for _ in range(NUM_PEOPLE):
            person = PersonFactory()
            people.append(person)

        interviews = []
        # Create interviews
        for _ in range(NUM_PEOPLE):
            interview = InterviewFactory()
            interviews.append(interview)

        # Create locations
        locations = []
        for _ in range(NUM_LOCATIONS):
            location = LocationFactory()
            locations.append(location)
